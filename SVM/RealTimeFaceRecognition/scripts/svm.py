"""
Auther: Chenxing Ouyang <c2ouyang@ucsd.edu>
This file is part of Cogs 109 Project.
Summary: SVM methods using Scikit
"""

import cv2
import os
import numpy as np
from scipy import ndimage
from time import time
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from sklearn.cross_validation import train_test_split
    #from sklearn.cross_validation import LeaveOneOut


from sklearn.datasets import fetch_lfw_people
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import SVC



def test_SVM(face_profile_data, face_profile_name_index, face_dim, face_profile_names):
    """
    Pruebas: Construir el modelo los SVM clasificacion utilizando la matriz face_profile_data ( numOfFace X numOfPixel ) y la matriz face_profile_name_index , face_dim es una tupla de la dimension de cada imagen ( h , w ) Devuelve el modle SVM clasificacion
    Parameters
    ----------
    face_profile_data : ndarray (number_of_images_in_face_profiles, width * height of the image)
        The pca that contains the top eigenvectors extracted using approximated Singular Value Decomposition of the data

    face_profile_name_index : ndarray
        The name corresponding to the face profile is encoded in its index

    face_dim : tuple (int, int)
        The dimension of the face data is reshaped to

    face_profile_names: ndarray
        The names corresponding to the face profiles
    Returns
    -------
    parametros

    face_profile_data: ndarray (number_of_images_in_face_profiles, ancho * altura de la imagen)
    el pca que contiene los principales vectores propios extraido por medio de la aproximacion descomposicion en valores singulares de los datos

    face_profile_name_index: ndarray
    El nombre correspondiente al perfil de la cara esta codificada en su indice
    face_dim: tupla (int, int)
    La dimension de los datos faciales se forma de nuevo a

    face_profile_names: ndarray
    Los nombres correspondientes a los perfiles de la cara
    Devoluciones
    -----
    clf : theano object
    The trained SVM classification model

    pca : theano ojbect
    The pca that contains the top 15 eigenvectors extracted using approximated Singular Value Decomposition of the data

    CLF: Objeto de Teano
    El modelo de clasificacion SVM
    PCA: Teano ojbect
    El PCA que contiene los 15 primeros vectores propios extraido por medio de la aproximacion descomposicion en valores singulares de los datos
    """
    X = face_profile_data
    y = face_profile_name_index



    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42) #Validacion cruzada
    #Ocupa un 25% de los datos para pruebas
    
    # Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled
    # dataset): unsupervised feature extraction / dimensionality reduction
    # Calcular PCA (Eigenfaces) en el conjunto de datos de la cara (se trata como sin marcar
    # Conjunto de datos): extraccion de caracteristicas sin supervision / reduccion de dimensionalidad
    n_components = 24 # maximum number of components to keep

    print("\n Extraccion de las mejores %d  Eigenfaces de  %d rostros" % (n_components, X_train.shape[0]))
    #print("\nExtracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0]))

    pca = RandomizedPCA(n_components=n_components, whiten=True).fit(X_train)
    eigenfaces = pca.components_.reshape((n_components, face_dim[0], face_dim[1]))

    # This portion of the code is used if the data is scarce, it uses the number 
    # of imputs as the number of features
    # Esta parte del codigo se utiliza si los datos son escasos, se utiliza el numero de
    # De insumos como el numero de caracteristicas
    # pca = RandomizedPCA(n_components=None, whiten=True).fit(X_train)
    # eigenfaces = pca.components_.reshape((pca.components_.shape[0], face_dim[0], face_dim[1]))

    #print("\nProjecting the input data on the eigenfaces orthonormal basis")
    print("\nLa proyeccion de los datos de entrada en las bases ortonormales Eigenfaces")
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test) 

    # Train a SVM classification model

    #print("\nFitting the classifier to the training set")
    print("\nMontaje del clasificador para el conjunto de entrenamiento")
    param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
                  'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
    # clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
    # Train_pca Test Error Rate:  0.0670016750419
    # Train_pca Test Recognition Rate:  0.932998324958



    # clf = SVC(kernel='linear', C=1)
    # 2452  samples from  38  people are loaded
    # Extracting the top 15 eigenfaces from 1839 faces
    # Extracting the top 15 eigenfaces from 1790 faces
    # Train_pca Test Error Rate:  0.0904522613065
    # Train_pca Test Recognition Rate:  0.909547738693

    # clf = SVC(kernel='poly')
    # Train_pca Test Error Rate:  0.201005025126
    # Train_pca Test Recognition Rate:  0.798994974874

    # clf = SVC(kernel='sigmoid')
    # Train_pca Test Error Rate:  0.985318107667
    # Train_pca Test Recognition Rate:  0.0146818923328
    

    # clf = SVC(kernel='rbf').fit(X_train, y_train)
    # Train_pca Test Error Rate:  0.0619765494137
    # Train_pca Test Recognition Rate:  0.938023450586



    # Best Estimator found using Radial Basis Function Kernal:
    clf = SVC(C=1000.0, cache_size=200, class_weight='balanced', coef0=0.0,
  decision_function_shape=None, degree=3, gamma=0.0001, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
    # Train_pca with Alex Test Error Rate:  0.088424437299
    # Train_pca with Alex Test Recognition Rate:  0.911575562701  0.91XX75562701

    clf = clf.fit(X_train_pca, y_train)
    # print("\nBest estimator found by grid search:")
    # print(clf.best_estimator_)
    # print("\nMejor estimacion encontrado por busqueda de cuadricula:")
    # print(clf.best_estimator_)

    ###############################################################################
    # Quantitative evaluation of the model quality on the test set
    # La evaluacion cuantitativa de la calidad del modelo en el equipo de prueba
    #print("\nPredicting people's names on the test set")
    print("\nPrediciendo nombres de las personas en el conjunto de prueba")
    t0 = time()
    y_pred = clf.predict(X_test_pca)
    #print("\nPrediction took %0.8f second per sample on average" % ((time() - t0)/y_pred.shape[0]*1.0))
    print("\nherramienta de Prediccion %0.8f segundos por muestra, en promedio" % ((time() - t0)/y_pred.shape[0]*1.0))

    # print "predicated names: ", y_pred
    # print "actual names: ", y_test
    error_rate = errorRate(y_pred, y_test)
    print ("\nTest Error Rate: %0.4f %%" % (error_rate * 100))
    print ("Test Recognition Rate: %0.4f %%" % ((1.0 - error_rate) * 100))
    
    ###############################################################################
    # Testing
    # Pruebas

    X_test_pic1 = X_test[0]
    X_test_pic1_for_display = np.reshape(X_test_pic1, face_dim)

    t0 = time()
    pic1_pred_name = predict(clf, pca, X_test_pic1, face_profile_names)
    #print("\nPrediction took %0.3fs" % (time() - t0))
    #print "\nPredicated result for picture_1 name: ", pic1_pred_name
    print("\nPrediccion tomo %0.3fs" % (time() - t0))
    print "\nresultado previsto para el nombre Picture_1: ", pic1_pred_name
    for i in range(1,3): print ("\n")

    import matplotlib.pyplot as plt
    # Display the picture
    # Visualizar la imagen
    plt.figure(1)
    plt.title(pic1_pred_name)
    plt.subplot(111)
    plt.imshow(X_test_pic1_for_display)
    plt.show()


    ###############################################################################
    # Qualitative evaluation of the predictions using matplotlib
    # Evaluacion cualitativa de las predicciones utilizando matplotlib
    

    def plot_gallery(images, titles, face_dim, n_row=3, n_col=4):
        """Helper function to plot a gallery of portraits"""
        """Funcion de ayuda para trazar una galeria de retratos"""
        plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
        plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
        for i in range(n_row * n_col):
            plt.subplot(n_row, n_col, i + 1)
            plt.imshow(images[i].reshape(face_dim), cmap=plt.cm.gray)
            plt.title(titles[i], size=12)
            plt.xticks(())
            plt.yticks(())


    # plot the result of the prediction on a portion of the test set
    # trazar el resultado de la prediccion en una parte del equipo de prueba

    def title(y_pred, y_test, face_profile_names, i):
        pred_name = face_profile_names[y_pred[i]].rsplit(' ', 1)[-1]
        true_name = face_profile_names[y_test[i]].rsplit(' ', 1)[-1]
        #return 'predicted: %s\ntrue:      %s' % (pred_name, true_name)
        return 'predicciones: %s\nverdaderos:      %s' % (pred_name, true_name)

    prediction_titles = [title(y_pred, y_test, face_profile_names, i)
                         for i in range(y_pred.shape[0])]

    plot_gallery(X_test, prediction_titles, face_dim)

    # plot the gallery of the most significative eigenfaces

    eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
    plot_gallery(eigenfaces, eigenface_titles, face_dim)

    plt.show()


    return clf, pca


def build_SVC(face_profile_data, face_profile_name_index, face_dim):
    """
    Build the SVM classification modle using the face_profile_data matrix (numOfFace X numOfPixel) and face_profile_name_index array, face_dim is a tuple of the dimension of each image(h,w) Returns the SVM classification modle
    Parameters
    ----------
    face_profile_data : ndarray (number_of_images_in_face_profiles, width * height of the image)
        The pca that contains the top eigenvectors extracted using approximated Singular Value Decomposition of the data

    face_profile_name_index : ndarray
        The name corresponding to the face profile is encoded in its index

    face_dim : tuple (int, int)
        The dimension of the face data is reshaped to

    Returns
    -------
    clf : theano object
        The trained SVM classification model

    pca : theano ojbect
        The pca that contains the top 15 eigenvectors extracted using approximated Singular Value Decomposition of the data

    """

    X = face_profile_data
    y = face_profile_name_index

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    #print "face_profile_data=",face_profile_data
    #print "face_profile_name_index=",face_profile_name_index
    #print "X_train=",X_train
    #print "X_test=",X_test
    #print "y_train=",y_train
    #print "y_test=",y_test
    # Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled
    # dataset): unsupervised feature extraction / dimensionality reduction
    n_components = 24  # maximum number of components to keep

    print("\n Extraccion de las mejores %d  Eigenfaces de  %d rostros" % (n_components, X_train.shape[0]))
    #print("\nExtracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0]))

    pca = RandomizedPCA(n_components=n_components, whiten=True).fit(X_train)
    eigenfaces = pca.components_.reshape((n_components, face_dim[0], face_dim[1]))

    # This portion of the code is used if the data is scarce, it uses the number 
    # of imputs as the number of features
    # pca = RandomizedPCA(n_components=None, whiten=True).fit(X_train)
    # eigenfaces = pca.components_.reshape((pca.components_.shape[0], face_dim[0], face_dim[1]))
    
    print("\nProyeccion de los datos de entrada en base a los Eigenfaces ortonormales")
    #print("\nProjecting the input data on the eigenfaces orthonormal basis")
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test) 

    # Train a SVM classification model

    print("\nMontaje del clasificador para el conjunto de entrenamiento")
    #print("\nFitting the classifier to the training set")
    param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
                  'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
    # clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)

    # Best Estimator found using Radial Basis Function Kernal: rbf sigmoid poly linear
    clf = SVC(C=1000.0, cache_size=200, class_weight='balanced', coef0=0.0,
  decision_function_shape=None, degree=4, gamma=0.0001, kernel='linear',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
    # Train_pca with Alex Test Error Rate:  0.088424437299
    # Train_pca with Alex Test Recognition Rate:  0.911575562701

    clf = clf.fit(X_train_pca, y_train)
    # print("\nBest estimator found by grid search:")
    # print(clf.best_estimator_)

    ###############################################################################
    # Quantitative evaluation of the model quality on the test set
    print("\nPrediccion de nombres de las personas en el conjunto de prueba")
    #print("\nPredicting people's names on the test set")
    t0 = time()
    y_pred = clf.predict(X_test_pca)
    print("\nLa prediccion tomo %s seg por muestra en promedio" % ((time() - t0)/y_pred.shape[0]*1.0))
    #print("\nPrediction took %s per sample on average" % ((time() - t0)/y_pred.shape[0]*1.0))
    #print "predicated names: ", y_pred
    #print "actual names: ", y_test
    error_rate = errorRate(y_pred, y_test)
    print ("\nPrueba de tasa de error: %0.4f %%" % (error_rate * 100))
    #print ("\nTest Error Rate: %0.4f %%" % (error_rate * 100))
    print ("Tasa Prueba de Reconocimiento : %0.4f %%" % ((1.0 - error_rate) * 100))
    #print ("Test Recognition Rate: %0.4f %%" % ((1.0 - error_rate) * 100))
    return clf, pca


def predict(clf, pca, img, face_profile_names):
    """
    Predict the name of the supplied image from the list of face profile names

    Parameters
    ----------
    clf: theano object
        The trained svm classifier 

    pca: theano object
        The pca that contains the top eigenvectors extracted using approximated Singular Value Decomposition of the data

    img: ndarray
        The input image for prediction

    face_profile_names: list
       The names corresponding to the face profiles
    Returns
    -------
    name : string
        The predicated name


        Predecir el nombre de la imagen suministrada por la lista de nombres de perfil cara
    parametros
    ----------
    CLF: Objeto de Teano
    El clasificador SVM
    PCA: Objeto de Teano
    El PCA que contiene los principales vectores propios extraido por medio de la aproximacion descomposicion en valores singulares de los datos
    img: ndarray
    La imagen de entrada para la prediccion
    face_profile_names: lista
    Los nombres correspondientes a los perfiles de la cara
    Devoluciones
    -------
    Nombre: Cadena
    El nombre hendida

    """

    img = img.ravel()
    # Apply dimentionality reduction on img, img is projected on the first principal components previous extracted from the Yale Extended dataset B.
    # Aplicar la reduccion de dimensionalidad en IMG, IMG se proyecta en los primeros componentes principales anteriores extraidos de la base de datos
    principle_components = pca.transform(img)
    pred = clf.predict(principle_components) 
    name = face_profile_names[pred]
    return name

def errorRate(pred, actual):
    """
    Calculate name prediction error rate  //Calcula nombre de tasa de error de prediccion

    Parameters //Parametros
    ----------
    pred: ndarray (1, number_of_images_in_face_profiles) // (1, numero de imagenes en los perfiles de la cara)
        The predicated names of the test dataset //Los nombres predichas de los datos de prueba

    actual: ndarray (1, number_of_images_in_face_profiles)
        The actual names of the test dataset //Los nombres reales de los datos de prueba

    Returns
    -------
    error_rate: float //tasa de error:
        The calcualted error rate //La tasa de error calculado

    """
    if pred.shape != actual.shape: return None
    error_rate = np.count_nonzero(pred - actual)/float(pred.shape[0])
    return error_rate


