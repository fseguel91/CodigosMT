""" 
========================================================
    Reconocimiento y deteccion de rostros usando OpenCV 
========================================================

Resumen: En tiempo real  seguimiento facial y reconocimiento usando harrcascade y SVM

Ejecutar: * Para ejecutarlo sin opciones    main.py python
        O corriendo con opciones (Por defecto, scale_multiplier = 4):
        main.py python [scale_multiplier = <screensize dividido por scale_multiplier>]
        Decir que desea ejecutar con 1/2 del tamamo completo sreen, especifique que scale_multiplier = 4:
        python main.py 4
Uso:
        pulse 'q' o 'ESC' para salir de la aplicacion
"""
#The dataset used is the Extended Yale Database B Cropped
 # http://vision.ucsd.edu/~leekc/ExtYaleDatabase/ExtYaleB.html
#Summary:
#        Real time facial tracking and recognition using harrcascade 
#        and SVM
#To Run:
#    * To run it without options
#        python main.py
#    * Or running with options (By default, scale_multiplier = 4):
 #       python main.py [scale_multiplier=<full screensize divided by scale_multiplier>]
#    * Say you want to run with 1/2 of the full sreen size, specify that scale_multiplier = 4:
#        python main.py 4
#Usage: 
#        press 'q' or 'ESC' to quit the application
#Auther: Chenxing Ouyang <c2ouyang@ucsd.edu>

import cv2
import os
import numpy as np
from scipy import ndimage
from time import time
import matplotlib.pyplot as plt
import utils as ut
import svm
import sys
import logging
import warnings


print(__doc__)

###############################################################################
# Building SVC from database

FACE_DIM = (50,50) # h = 50, w = 50

# Load training data from face_profiles/   Cargar datos de entrenamiento de face_profiles /
face_profile_data, face_profile_name_index, face_profile_names  = ut.load_training_data("../face_profiles/")

print "\n", face_profile_name_index.shape[0], " fotografias de ", len(face_profile_names), " personas estan cargadas"

# Build the classifier  // Construir el clasificador
clf, pca = svm.build_SVC(face_profile_data, face_profile_name_index, FACE_DIM)
#clf, pca = svm.test_SVM(face_profile_data, face_profile_name_index, FACE_DIM, face_profile_names)

###############################################################################
# Facial Recognition In Live Tracking  //Reconocimiento Facial con seguimiento en linea


DISPLAY_FACE_DIM = (200, 200) # the displayed video stream screen dimention // el video se muestra la pantalla corriente Dimension
SKIP_FRAME = 2      # the fixed skip frame //el marco de salto fijo
frame_skip_rate = 0 # skip SKIP_FRAME frames every other frame //enmarca cada dos fotogramas
SCALE_FACTOR = 4 # used to resize the captured frame for face detection for faster processing speed 
#Cambia Tamano de ventana utilizarlo para cambiar el tamano del fotograma capturado de deteccion de rostros para mayor velocidad de procesamiento
face_cascade = cv2.CascadeClassifier("../classifier/haarcascade_frontalface_default.xml") #create a cascade classifier //crear un clasificador cascada
sideFace_cascade = cv2.CascadeClassifier('../classifier/haarcascade_profileface.xml')

if len(sys.argv) == 2: 
    SCALE_FACTOR = float(sys.argv[1]) #Asigna nuevo Factor de escala
elif len(sys.argv) >2:
    logging.error("main.py ")
# dictionary mapping used to keep track of head rotation maps //
#mapeo  utiliza para realizar un seguimiento de los mapas de rotacion de la cabeza
rotation_maps = {
    "left": np.array([-30, 0, 30]),
    "right": np.array([30, 0, -30]),
    "middle": np.array([0, -30, 30]),
}

def get_rotation_map(rotation):
    """ Toma en un angulo de rotacion, y devuelve una rotacion de mapas optimizado """   #""" Takes in an angle rotation, and returns an optimized rotation map """
    if rotation > 0: return rotation_maps.get("right", None)
    if rotation < 0: return rotation_maps.get("left", None)
    if rotation == 0: return rotation_maps.get("middle", None)

current_rotation_map = get_rotation_map(0) 


webcam = cv2.VideoCapture(0)

ret, frame = webcam.read() # get first frame // conseguir primer cuadro
frame_scale = (frame.shape[1]/SCALE_FACTOR,frame.shape[0]/SCALE_FACTOR)  # (y, x)

cropped_face = []
num_of_face_saved = 0


while ret:
    key = cv2.waitKey(1)
    # exit on 'q' 'esc' 'Q' //salida a la 'q' 'esc' 'Q'
    if key in [27, ord('Q'), ord('q')]: 
        break
    # resize the captured frame for face detection to increase processing speed // 
    # cambiar el tamano del fotograma capturado para la deteccion de cara a aumentar la velocidad de procesamiento
    resized_frame = cv2.resize(frame, frame_scale)

    processed_frame = resized_frame
    # Skip a frame if the no face was found last frame // Saltar de un marco de la cara no se encontro ultimo fotograma

    if frame_skip_rate == 0:
        faceFound = False
        for rotation in current_rotation_map:

            rotated_frame = ndimage.rotate(resized_frame, rotation)

            gray = cv2.cvtColor(rotated_frame, cv2.COLOR_BGR2GRAY)

            # return tuple is empty, ndarray if detected face // retorno tupla esta vacia, array si se detecta la cara
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            ) 

            # If frontal face detector failed, use profileface detector 
            # // Si la deteccion de caras frontal fallo, perfil de usuario cara de deteccion otro xml
            faces = faces if len(faces) else sideFace_cascade.detectMultiScale(                
                gray,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            # for f in faces:
            #     x, y, w, h = [ v*SCALE_FACTOR for v in f ] # scale the bounding box back to original frame size // escalar el cuadro delimitador de nuevo a tamano trama original
            #     cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0))
            #     cv2.putText(frame, "DumbAss", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))

            if len(faces):
                for f in faces:
                    # Crop out the face // Recortar la cara
                    x, y, w, h = [ v for v in f ] # scale the bounding box back to original frame size // 
                    # escalar el cuadro delimitador de nuevo a tamano trama original
                    cropped_face = rotated_frame[y: y + h, x: x + w]   # img[y: y + h, x: x + w]
                    cropped_face = cv2.resize(cropped_face, DISPLAY_FACE_DIM, interpolation = cv2.INTER_AREA)

                    # Name Prediction // Prediccion Nombre 
                    face_to_predict = cv2.resize(cropped_face, FACE_DIM, interpolation = cv2.INTER_AREA)
                    face_to_predict = cv2.cvtColor(face_to_predict, cv2.COLOR_BGR2GRAY) #Imagen recorta a escala grises
                    name_to_display = svm.predict(clf, pca, face_to_predict, face_profile_names)
                    #ocupa svm.py donde predice el nombre de la imagen suministrada

                    # Display frame // marco de la pantalla
                    cv2.rectangle(rotated_frame, (x,y), (x+w,y+h), (0,255,0))
                    cv2.putText(rotated_frame, name_to_display, (x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,255,0))

                # rotate the frame back and trim the black paddings
                processed_frame = ut.trim(ut.rotate_image(rotated_frame, rotation * (-1)), frame_scale)

                # reset the optmized rotation map
                current_rotation_map = get_rotation_map(rotation)

                faceFound = True


                break

        if faceFound: 
            frame_skip_rate = 0
            # print "Face Found"
        else:
            frame_skip_rate = SKIP_FRAME
            # print "Face Not Found"

    else:
        frame_skip_rate -= 1
        # print "Face Not Found"


    # print "Frame dimension: ", processed_frame.shape
  
    cv2.putText(processed_frame, "Presiona ESC o 'q' para salir.", (5, 15),
            cv2.FONT_HERSHEY_PLAIN, 0.5, (255,255,255))

    cv2.imshow("Reconocimiento de Caras en Tiempo Real Frame Procesados:", processed_frame)



    if len(cropped_face):
        cv2.imshow("Cara recortada", cv2.cvtColor(cropped_face, cv2.COLOR_BGR2GRAY))
        face_to_predict = cv2.resize(cropped_face, FACE_DIM, interpolation = cv2.INTER_AREA)
        face_to_predict = cv2.cvtColor(face_to_predict, cv2.COLOR_BGR2GRAY)
        name_to_display = svm.predict(clf, pca, face_to_predict, face_profile_names)
    # get next frame
    ret, frame = webcam.read()


webcam.release()
cv2.destroyAllWindows()


