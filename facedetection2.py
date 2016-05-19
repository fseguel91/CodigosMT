import SimpleCV               #Importa funciones de SimpleCV
from wand.image import Image  #Importa de Image la funcion de MagickWand
                                                #(Permite cambiar el formato)
                                                # $apt-get install libmagickwand-dev
                                                # $ pip install Wand

cam = SimpleCV.Camera()       #Se abre el software de la camara para trabajar con SimpleCV
count = 1                     #Inicializacion de variable
while count<6:       
   img = cam.getImage()       #Se toma una imagen de la camara
   faces = img.findHaarFeatures('face.xml')  #Busqueda caracteristicas Haar de ViolaJones
   if faces is not None:
      faces = faces.sortArea()
      bigFace = faces[-1]     #Se obtiene la cara mas grande
      bigFace.draw()          #Se dibuja el rectangulo verde
      x,y,w,h = bigFace.boundingBox()  #boundingBox devuelve las coordenadas de las esquias del rectangulo
      cara = img.crop(x,y,w,h)   #Recortamos la imagen
      cara = cara.resize(220,233)   #Redimensionamos
      cara.save('cara' + str(count) + '.png')   #Guadamos la cara en formato PNG
		OriginalImagen.format = 'gif'
		OriginalImagen.save(filename='caraGIF' + str(count) + '.gif') #Se ocupa MagickWand para cambiar formato de imagen
      count = count + 1 #Aumentamos el contador y se repite el ciclo
   img.show()


