"""
Auther: Chenxing Ouyang <c2ouyang@ucsd.edu>

This file is part of Cogs 109 Project.

Summary: Utilties used for facial tracking in OpenCV 

"""


import cv2
import numpy as np
from scipy import ndimage
import os
import errno
import sys
import logging
import shutil


###############################################################################
# Used For Facial Tracking and Traning in OpenCV // Utilizado para el seguimiento facial y la formacion en OpenCV

def read_images_from_single_face_profile(face_profile, face_profile_name_index, dim = (50, 50)):
    """
    Reads all the images from one specified face profile into ndarrays //
    Lee todas las imagenes de un perfil de la cara especificada en ndarrays

    Parameters
    ----------
    face_profile: string //Perfil de la cara
        The directory path of a specified face profile // La ruta del directorio de un perfil de una cara especifica
        

    face_profile_name_index: int
        The name corresponding to the face profile is encoded in its index 
        //El nombre correspondiente al perfil de la cara esta codificada en su indice

    dim: tuple = (int, int)
        The new dimensions of the images to resize to // Las nuevas dimensiones de las imagenes para cambiar el tamano de

    Returns
    -------
    X_data : numpy array, shape = (number_of_faces_in_one_face_profile, face_pixel_width * face_pixel_height)
        A face data array contains the face image pixel rgb values of all the images in the specified face profile 
        //Una matriz de datos de cara contiene los valores RGB cara pixeles de la imagen de todas las imagenes 
        en el perfil de la cara especificada
    Y_data : numpy array, shape = (number_of_images_in_face_profiles, 1) //numero de imagenes en los perfiles de la cara
        A face_profile_index data array contains the index of the face profile name of the specified face profile directory
        //Una matriz de datos del indice de perfil de la cara contiene el indice del nombre del perfil de la cara
         del directorio del perfil de una cara especifica
    """
    X_data = np.array([])
    index = 0
    for the_file in os.listdir(face_profile):
        file_path = os.path.join(face_profile, the_file)
        # Se puede agregar extension
        if file_path.endswith(".png") or file_path.endswith(".jpg") or file_path.endswith(".jpeg") or file_path.endswith(".pgm") or file_path.endswith(".gif"):
            img = cv2.imread(file_path, 0)
            img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            img_data = img.ravel()
            X_data = img_data if not X_data.shape[0] else np.vstack((X_data,img_data))
            index += 1

    if index == 0 : 
        shutil.rmtree(face_profile)
        logging.error("\nExiste perfiles de cara sin imagenes")
        #logging.error("\nThere exists face profiles without images")

    Y_data = np.empty(index, dtype = int)
    Y_data.fill(face_profile_name_index)
    return X_data, Y_data

def delete_empty_profile(face_profile_directory):
    """
    Deletes empty face profiles in face profile directory and logs error if face profiles contain too little images
    //Eliminar los perfiles faciales vacias en el directorio perfil de la cara y los registros de error si los perfiles faciales contienen demasiado pequenas imagenes
    Parameters
    ----------
    face_profile_directory: string
        The directory path of the specified face profile directory //La ruta del directorio del directorio de perfil de una cara especifica

    """
    for face_profile in os.listdir(face_profile_directory):
        if "." not in str(face_profile):
            face_profile = os.path.join(face_profile_directory, face_profile)
            index = 0
            for the_file in os.listdir(face_profile):
                file_path = os.path.join(face_profile, the_file)
                if file_path.endswith(".png") or file_path.endswith(".jpg") or file_path.endswith(".jpeg") or file_path.endswith(".pgm") or file_path.endswith(".gif"):
                    index += 1
            if index == 0 : 
                shutil.rmtree(face_profile)
                print "\nEliminado ", face_profile, " ya que no contiene imagenes"
                #print "\nDeleted ", face_profile, " because it contains no images"
            if index < 2 : 
                logging.error("\nperfil de la cara " + str(face_profile) + " contiene tambien pequenas imagenes (se necesitan al menos 2 imagenes)")
                #logging.error("\nFace profile " + str(face_profile) + " contains too little images (At least 2 images are needed)")


def load_training_data(face_profile_directory):
    """
    Loads all the images from the face profile directory into ndarrays
    //Cargas todas las imagenes del directorio de perfil cara en ndarrays

    Parameters
    ----------
    face_profile_directory: string
        The directory path of the specified face profile directory 
        //La ruta del directorio del directorio de perfil de una cara especifica

    face_profile_names: list
        The index corresponding to the names corresponding to the face profile directory
        //El indice correspondiente a los nombres correspondientes en el directorio de perfil de la cara

    Returns
    -------
    X_data : numpy array, shape = (number_of_faces_in_face_profiles, face_pixel_width * face_pixel_height)
        A face data array contains the face image pixel rgb values of all face_profiles

    Y_data : numpy array, shape = (number_of_face_profiles, 1)
        A face_profile_index data array contains the indexs of all the face profile names

    """
    delete_empty_profile(face_profile_directory)  # delete profile directory without images 
    #Eliminar el directorio del perfil sin imagenes

    # Get a the list of folder names in face_profile as the profile names
    # Obtener una lista de los nombres de las carpetas en face_profile como los nombres de los perfiles
    face_profile_names = [d for d in os.listdir(face_profile_directory) if "." not in str(d)]

    if len(face_profile_names) < 2:
        logging.error("\nPerfil de la cara contiene demasiado poco perfiles (se necesitan al menos 2 perfiles)")
        #logging.error("\nFace profile contains too little profiles (At least 2 profiles are needed)")
        exit()

    first_data = str(face_profile_names[0])
    first_data_path = os.path.join(face_profile_directory, first_data)
    X1, y1 = read_images_from_single_face_profile(first_data_path, 0)
    X_data = X1   
    Y_data = y1   
    print "Cargando Base de datos: "
    print 0, "    ",X1.shape[0]," imagenes se cargan a partir de:", first_data_path
    #print "Loading Database: "
    #print 0, "    ",X1.shape[0]," images are loaded from:", first_data_path
    for i in range(1, len(face_profile_names)):
        directory_name = str(face_profile_names[i])
        directory_path = os.path.join(face_profile_directory, directory_name)
        tempX, tempY = read_images_from_single_face_profile(directory_path, i)
        X_data = np.concatenate((X_data, tempX), axis=0)
        Y_data = np.append(Y_data, tempY)
        print i, "    ",tempX.shape[0]," imagenes se cargan a partir de:", directory_path
        #print i, "    ",tempX.shape[0]," images are loaded from:", directory_path

    return X_data, Y_data, face_profile_names


def rotate_image(img, rotation, scale = 1.0):
    """
    Rotate an image rgb matrix with the same dimensions
    #Girar una matriz de imagen RGB con las mismas dimensiones

    Parameters
    ----------
    image: string
        the image rgb matrix
        #la matriz de la imagen RGB

    rotation: int
        The rotation angle in which the image rotates to
        #El angulo de rotacion en el que la imagen girada a

    scale: float
        The scale multiplier of the rotated image
        #El multiplicador de escala de la imagen girada

    Returns
    -------
    rot_img : numpy array
        Rotated image after rotation
        #Rotar la imagen despues de la rotacion

    """
    if rotation == 0: return img
    h, w = img.shape[:2]
    rot_mat = cv2.getRotationMatrix2D((w/2, h/2), rotation, scale)
    rot_img = cv2.warpAffine(img, rot_mat, (w, h), flags=cv2.INTER_LINEAR)
    return rot_img

def trim(img, dim):
    """
    Trim the four sides(black paddings) of the image matrix and crop out the middle with a new dimension
    #Recorte los cuatro lados (Juntas negras) de la matriz de la imagen y recortar el centro con una nueva dimension
    Parameters
    ----------
    img: string
        the image rgb matrix
        #la matriz de la imagen RGB

    dim: tuple (int, int)
        The new dimen the image is trimmed to
        #Las nuevas dimen la imagen se recorta para

    Returns
    -------
    trimmed_img : numpy array
        The trimmed image after removing black paddings from four sides

    """

    # if the img has a smaller dimension then return the origin image
    if dim[1] >= img.shape[0] and dim[0] >= img.shape[1]: return img
    x = int((img.shape[0] - dim[1])/2) + 1
    y = int((img.shape[1] - dim[0])/2) + 1
    trimmed_img = img[x: x + dim[1], y: y + dim[0]]   # crop the image
    return trimmed_img



def clean_directory(face_profile):
    """
    Deletes all the files in the specified face profile

    Parameters
    ----------
    face_profile: string
        The directory path of a specified face profile

    """

    for the_file in os.listdir(face_profile):
        file_path = os.path.join(face_profile, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception, e:
            print e


def create_directory(face_profile):
    """
    Create a face profile directory for saving images

    Parameters
    ----------
    face_profile: string
        The directory path of a specified face profile

    """
    try:
        print "Making directory"
        os.makedirs(face_profile)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            print "The specified face profile already existed, it will be override"
            raise

def create_profile_in_database(face_profile_name, database_path="../face_profiles/", clean_directory=False):
    """
    Create a face profile directory in the database 

    Parameters
    ----------
    face_profile_name: string
        The specified face profile name of a specified face profile folder

    database_path: string
        Default database directory

    clean_directory: boolean
        Clean the directory if the user already exists

    Returns
    -------
    face_profile_path: string
        The path of the face profile created

    """
    face_profile_path = database_path + face_profile_name + "/"
    create_directory(face_profile_path)
    # Delete all the pictures before recording new
    if clean_directory: 
        clean_directory(face_profile_path) 
    return face_profile_path



