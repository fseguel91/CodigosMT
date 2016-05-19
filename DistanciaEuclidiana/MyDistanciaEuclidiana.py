""" 
====================================================
    Faces recognition usando DistanciaEuclidiana 
====================================================

Run: Para correr el codigo es necesario escribir en consola 

python MyDistanciaEuclidiana.py [DirectorioCaraReconocer]

Por ejemplo: python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s01Normal7.gif
			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s02Normal4.gif
			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s03Normal4.gif
 			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s04Normal1.gif
 			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s05Normal5.gif
 			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s06Normal5.gif     #-->No Funciona
 			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s07Normal3.gif	    #-->No Funciona
  			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s08Normal5.gif
 			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s09Normal1.gif
 			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s10Normal1.gif   		
			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s11Normal4.gif		#-->No Funciona
			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s12Normal1.gif	
			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s13Normal4.gif
 			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s14Normal2.gif		#-->No Funciona	
 			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s16Normal1.gif
 			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s18Normal1.gif
 			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s19Normal8.gif		#-->No Funciona
 			python MyDistanciaEuclidiana.py /home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/s11Normal1.gif		#-->No Funciona


 Autor: Felipe A. Seguel Mora felipeseguel@udec.cl  GibHub: https://github.com/fseguel91/Reconocimiento-de-Rostros-
"""
import numpy as np
from numpy import linalg as LA
import sys
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average

#Funcion Principal 

def main():

	NumerodeImagenesBD = 18
	#Carga Imagenes de Entrenamiento.
	img1 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageAAlarcon.png','png')
	img2 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageACarrasco.png','png')
	img3 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageASoto.png','png')
	img4 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageCLeal.png','png')
	img5 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageCmaldonado.png','png')
	img6 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageDPalacios.png','png')
	img7 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageDPerez.png','png')
	img8 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageDRamirez.png','png')
	img9 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageEtramon.png','png')
	img10 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageFMarin.png','png')
	img11 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageFQuiroz.png','png')
	img12 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageFSeguel.png','png')
	img13 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageMGeneral.png','png')
	img14 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averagePRiquelme.png','png')
	img15 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averagePRodriguez.png','png')
	img16 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageRDelgado.png','png')
	img17 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageSGogoy.png','png')
	img18 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageYIsla.png','png')
	#img19 = imread('/home/pi/Desktop/FacialRecognitionPython/DistanciaEuclidiana/averageSujetoNuevo.png','png')    # Agregar a un sujeto Nuevo

    #Carga de imagen de prueba
 	imgPrueba = imread(sys.argv[1],'gif')

	n_m1 = compare_images(img1, imgPrueba)
	n_m2 = compare_images(img2, imgPrueba)
	n_m3 = compare_images(img3, imgPrueba)
	n_m4 = compare_images(img4, imgPrueba)
	n_m5 = compare_images(img5, imgPrueba)
	n_m6 = compare_images(img6, imgPrueba)
	n_m7 = compare_images(img7, imgPrueba)
	n_m8 = compare_images(img8, imgPrueba)
	n_m9 = compare_images(img9, imgPrueba)
	n_m10 = compare_images(img10, imgPrueba)
	n_m11 = compare_images(img11, imgPrueba)
	n_m12 = compare_images(img12, imgPrueba)
	n_m13 = compare_images(img13, imgPrueba)
	n_m14 = compare_images(img14, imgPrueba)	
	n_m15 = compare_images(img15, imgPrueba)
	n_m16 = compare_images(img16, imgPrueba)
	n_m17 = compare_images(img17, imgPrueba)
	n_m18 = compare_images(img18, imgPrueba)

	MinDistancia = min(n_m1,n_m2,n_m3,n_m4,n_m5,n_m6,n_m7,n_m8,n_m9,n_m10,n_m11,n_m12,n_m13,n_m14,n_m15,n_m16,n_m17,n_m18)

	fig = plt.figure(1) 	# Show the original image
	plt.subplot(3, 6, 1)
	plt.imshow(img1, cmap = cm.Greys_r)
	plt.subplot(3, 6, 2)
	plt.imshow(img2, cmap = cm.Greys_r)
	plt.subplot(3, 6, 3)
	plt.imshow(img3, cmap = cm.Greys_r)
	plt.subplot(3, 6, 4)
	plt.imshow(img4, cmap = cm.Greys_r)
	plt.subplot(3, 6, 5)
	plt.imshow(img5, cmap = cm.Greys_r)
	plt.subplot(3, 6, 6)
	plt.imshow(img6, cmap = cm.Greys_r)
	plt.subplot(3, 6, 7)
	plt.imshow(img7, cmap = cm.Greys_r)
	plt.subplot(3, 6, 8)
	plt.imshow(img8, cmap = cm.Greys_r)
	plt.subplot(3, 6, 9)
	plt.imshow(img9, cmap = cm.Greys_r)
	plt.subplot(3, 6, 10)
	plt.imshow(img10, cmap = cm.Greys_r)
	plt.subplot(3, 6, 11)
	plt.imshow(img11, cmap = cm.Greys_r)
	plt.subplot(3, 6, 12)
	plt.imshow(img12, cmap = cm.Greys_r)
	plt.subplot(3, 6, 13)
	plt.imshow(img13, cmap = cm.Greys_r)
	plt.subplot(3, 6, 14)
	plt.imshow(img14, cmap = cm.Greys_r)
	plt.subplot(3, 6, 15)
	plt.imshow(img15, cmap = cm.Greys_r)
	plt.subplot(3, 6, 16)
	plt.imshow(img16, cmap = cm.Greys_r)
	plt.subplot(3, 6, 17)
	plt.imshow(img17, cmap = cm.Greys_r)
	plt.subplot(3, 6, 18)
	plt.imshow(img18, cmap = cm.Greys_r)
	plt.suptitle('Conjunto de Entrenamiento Base de Datos')
	

	plt.figure(2) # Plot imagen a Ingresar 
	plt.imshow(imgPrueba, cmap = cm.Greys_r)
	plt.title('Cara a Reconocer')
	
	plt.figure(3) # Resultado
	if MinDistancia == n_m1:
		plt.imshow(img1, cmap = cm.Greys_r)
		plt.title('Alvaro Alarcon; Distancia Euclidiana:'+ str(n_m1)+ '/ per pixel:'+ str(n_m1/img1.size))
	if MinDistancia == n_m2:
		plt.imshow(img2, cmap = cm.Greys_r)
		plt.title('Alejandro Carrasco; Distancia Euclidiana:'+ str(n_m2)+ '/ per pixel:'+ str(n_m2/img2.size))
	if MinDistancia == n_m3:
		plt.imshow(img3, cmap = cm.Greys_r)
		plt.title('Alvaro Soto; Distancia Euclidiana:'+ str(n_m3)+ '/ per pixel:'+ str(n_m3/img3.size))
	if MinDistancia == n_m4:
		plt.imshow(img4, cmap = cm.Greys_r)
		plt.title('Carlos Leal; Distancia Euclidiana:'+ str(n_m4)+ '/ per pixel:'+ str(n_m4/img4.size))
	if MinDistancia == n_m5:
		plt.imshow(img5, cmap = cm.Greys_r)
		plt.title('Caudio Maldonado; Distancia Euclidiana:'+ str(n_m5)+ '/ per pixel:'+ str(n_m5/img5.size))
	if MinDistancia == n_m6:
		plt.imshow(img6, cmap = cm.Greys_r)
		plt.title('Diego Palacios; Distancia Euclidiana:'+ str(n_m6)+ '/ per pixel:'+ str(n_m6/img6.size))
	if MinDistancia == n_m7:
		plt.imshow(img7, cmap = cm.Greys_r)
		plt.title('Diego Perez; Distancia Euclidiana:'+ str(n_m7)+ '/ per pixel:'+ str(n_m7/img7.size))
	if MinDistancia == n_m8:
		plt.imshow(img8, cmap = cm.Greys_r)
		plt.title('Diego Ramirez; Distancia Euclidiana:'+ str(n_m8)+ '/ per pixel:'+ str(n_m8/img8.size))
	if MinDistancia == n_m9:
		plt.imshow(img9, cmap = cm.Greys_r)
		plt.title('Emilio Tramon; Distancia Euclidiana:'+ str(n_m9)+ '/ per pixel:'+ str(n_m9/img9.size))
	if MinDistancia == n_m10:
		plt.imshow(img10, cmap = cm.Greys_r)
		plt.title('Felipe Marin; Distancia Euclidiana:'+ str(n_m10)+ '/ per pixel:'+ str(n_m10/img10.size))
	if MinDistancia == n_m11:
		plt.imshow(img11, cmap = cm.Greys_r)
		plt.title('Fabian Quiroz; Distancia Euclidiana:'+ str(n_m11)+ '/ per pixel:'+ str(n_m11/img11.size))
	if MinDistancia == n_m12:
		plt.imshow(img12, cmap = cm.Greys_r)
		plt.title('Felipe Seguel; Distancia Euclidiana:'+ str(n_m12)+ '/ per pixel:'+ str(n_m12/img12.size))
	if MinDistancia == n_m13:
		plt.imshow(img13, cmap = cm.Greys_r)
		plt.title('Mauricio General; Distancia Euclidiana:'+ str(n_m13)+ '/ per pixel:'+ str(n_m13/img13.size))
	if MinDistancia == n_m14:
		plt.imshow(img14, cmap = cm.Greys_r)
		plt.title('Pablo Riquelme; Distancia Euclidiana:'+ str(n_m14)+ '/ per pixel:'+ str(n_m14/img14.size))
	if MinDistancia == n_m15:
		plt.imshow(img15, cmap = cm.Greys_r)
		plt.title('Pablo Rodriguez; Distancia Euclidiana:'+ str(n_m15)+ '/ per pixel:'+ str(n_m15/img15.size))
	if MinDistancia == n_m16:
		plt.imshow(img16, cmap = cm.Greys_r)
		plt.title('Rene Delgado; Distancia Euclidiana:'+ str(n_m16)+ '/ per pixel:'+ str(n_m16/img16.size))
	if MinDistancia == n_m17:
		plt.imshow(img17, cmap = cm.Greys_r)
		plt.title('Sebastian Godoy; Distancia Euclidiana:'+ str(n_m17)+ '/ per pixel:'+ str(n_m17/img17.size))
	if MinDistancia == n_m18:
		plt.imshow(img18, cmap = cm.Greys_r)
		plt.title('Yurisam Isla; Distancia Euclidiana:'+ str(n_m18)+ '/ per pixel:'+ str(n_m18/img18.size))
	plt.show()

def compare_images(img1, img2):  # Normalizar para compensar la diferencia de exposicion, esto puede ser innecesario Considere desactivarlo
    img1 = normalize(img1)
    img2 = normalize(img2)
    m_norm = LA.norm(img1 - img2,2) 
    return (m_norm)

def normalize(arr):
	rng = arr.max()-arr.min()
	amin = arr.min()
	return (arr-amin)*255/rng

if __name__ == "__main__":
	main()

