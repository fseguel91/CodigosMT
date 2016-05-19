# CodigosMT
Se presentan todos los codigos desarrollados y modificados del Trabajo de Memoria de título Detección y Reconocimientos de Rostros en tiempo real usando plataforma Raspberry Pi para obtar a título de Ingeniero Civil en Telecomunicaciones

Licencia
========
Open Source


Instalación de SimpleCV en Raspberry Pi
=======================================

El procedimiento de instalación varia según cada sistema operativo. Para todas las opciones disponibles de Linux en la Raspberry Pi 
se siguen las instrucciones de la última versión estable se encuentra disponible en la página oficial de SimpleCV 
[www.simplecv.org/download/](www.simplecv.org/download/). 
Una vez que SimpleCV se encuentra instalado sin errores se debe ser capaz de abrir la ventana de consola escribiendo:

    pi@raspberrypi ~$ simplecv
 
##Los pasos para la instalación en Raspberry Pi:
    -Los pasos para la instalación en Raspberry Pi se puden encontrar en [https://github.com/sightmachine/SimpleCV/blob/develop/doc/HOWTO-Install%20on%20RaspberryPi.rst](https://github.com/sightmachine/SimpleCV/blob/develop/doc/HOWTO-Install%20on%20RaspberryPi.rst) y son básicamente:

-Encender la Raspberry Pi e ingresar:
    Username: pi
    Password: 


-Conectar la tarjeta a internet.
-Instalar las bibliotecas obligatorias ejecutando el siguiente comando para instalar las dependencias
    pi@raspberrypi ~$ sudo apt-get install ipython python-opencv python-scipy python-numpy python-setuptools python-pip

-SimpleCV ahora posee las dependencias necesarios para comenzar su instalación. El código fuente de SimpleCV se instala desde \textit{GitHub}.
	

    pi@raspberrypi ~$ sudo pip install https://github.com/sightmachine/SimpleCV/zipball/master

Debido a que la placa de Pi Cámara no es un dispositivo de video se hace necesario instalar el controlador $UV4L$. Esto hará que se convierta en un dispositivo de video, tal como una cámara USB. Para instalar el controlador se siguen los siguientes comandos.

    pi@raspberrypi ~ $ pkill uv4l
    pi@raspberrypi ~ $ uv4l --driver raspicam --auto-video_nr --encoding yuv420 --nopreview
    <notice> [core] Trying driver 'raspicam' from built-in drivers...
    <warning> [core] Driver 'raspicam' not found
    <notice> [core] Trying driver 'raspicam' from external plug-in s...
    <notice> [driver] Dual Raspicam Video4Linux2 Driver v1.9.32 built Sep 16 2015
    <notice> [driver] Selected format: 2592x1952, encoding: yuv420, YUV 4:2:0 Planar (I420)
    <notice> [driver] Framerate max. 30 fps
    <notice> [driver] ROI: 0, 0, 1, 1
    <notice> [core] Device detected!
    <notice> [core] Registering device node /dev/video0
    pi@raspberrypi ~ $ export LD_PRELOAD=/usr/lib/uv4l/uv4lext/armv6l/libuv4lext.so
    pi@raspberrypi ~ $ ls /dev/
    autofs           loop0               ptmx    root     tty20  tty4   tty59      vcs4
    block            loop1               pts     shm      tty21  tty40  tty6       vcs5
    btrfs-control    loop2               ram0    snd      tty22  tty41  tty60      vcs6
    bus              loop3               ram1    sndstat  tty23  tty42  tty61      vcsa
    cachefiles       loop4               ram10   stderr   tty24  tty43  tty62      vcsa1
    char             loop5               ram11   stdin    tty25  tty44  tty63      vcsa2
    console          loop6               ram12   stdout   tty26  tty45  tty7       vcsa3
    cpu_dma_latency  loop7               ram13   tty      tty27  tty46  tty8       vcsa4
    cuse             loop-control        ram14   tty0     tty28  tty47  tty9       vcsa5
    disk             MAKEDEV             ram15   tty1     tty29  tty48  ttyAMA0    vcsa6
    fb0              mapper              ram2    tty10    tty3   tty49  ttyprintk  vcsm
    fd               mem                 ram3    tty11    tty30  tty5   uinput     vhci
    full             memory_bandwidth    ram4    tty12    tty31  tty50  urandom    video0
    fuse             mmcblk0             ram5    tty13    tty32  tty51  vc-cma     xconsole
    gpiomem          mmcblk0p1           ram6    tty14    tty33  tty52  vchiq      zero
    hidraw0          mmcblk0p2           ram7    tty15    tty34  tty53  vcio
    hidraw1          net                 ram8    tty16    tty35  tty54  vc-mem
    hwrng            network_latency     ram9    tty17    tty36  tty55  vcs
    input            network_throughput  random  tty18    tty37  tty56  vcs1
    kmsg             null                raw     tty19    tty38  tty57  vcs2
    log              ppp                 rfkill  tty2     tty39  tty58  vcs3


Se puede ver que está el dispositivo $video0$ en la línea número 26. Finalizado este paso la Raspberry Pi está ejecutando SimpleCV utilizando la Pi-cam.



##Instalación de OpenCV 2.4.9 y paquetes Python en Raspbian

Este tipo de instalación es fundamental en todo proyecto que incluya procesamiento digital de imágenes. Se documenta este paso con el fin de que futuros interesados en el tema sorteen dificultades de manera más rápida.
El proceso para instalar OpenCV toma alrededor de 3 horas. Además se debe tomar en cuenta que esta instalación sin la limpieza de paquetes innecesarios en la Raspberry Pi ocupará un $90\%$ de la capacidad de una tarjeta microSD de $8$GB. Existen varias formas de instalación de OpenCV disponibles en Internet, siendo el tutorial guía la página [www.RoboPapa.com](www.RoboPapa.com)  en la cual se siguen los siguientes pasos:


-Paso 1: Lo primero es abrir una terminal para verificar si existen actualizaciones de los paquetes ya instalados en la Raspberry Pi para luego hacer una actualización de \textit{firmware}

    pi@raspberrypi $ sudo apt-get update
    pi@raspberrypi $ sudo apt-get upgrade
    pi@raspberrypi $ sudo rpi-update

La rapidez de esta operación dependerá de la conexión a Internet y del tiempo que haya pasado desde la última actualización.
	

-Paso 2: Luego se ejecutan los siguientes dos comandos que son la instalación de las herramientas y paquetes necesarios como la instalación de paquetes de imágenes \ac{I/O}, el cual permite la carga de imágenes en varios formatos JPEG, PNG, TIFF, etc., y la instalación de paquetes de videos \ac{I/O}, los cuales permiten la carga de archivos de video usando \ac{OpenCV} y se instalan las herramientas de desarrollo de \textit{Python}.

    pi@raspberrypi $ sudo apt-get -y install build-essential cmake cmake-curses-gui\
    pkg-config libpng12-0 libpng12-dev libpng++-dev libpng3\
    libpnglite-dev zlib1g-dbg zlib1g zlib1g-dev pngtools \
    libtiff4-dev libtiff4 libtiffxx0c2 libtiff-tools\
    libeigen3-dev



    pi@raspberrypi $ sudo apt-get -y install libjpeg8 libjpeg8-dev libjpeg8-dbg\
    libjpeg-progs ffmpeg libavcodec-dev libavcodec53 libavformat53\
    libavformat-dev libgstreamer0.10-0-dbg libgstreamer0.10-0\
    libgstreamer0.10-dev libxine1-ffmpeg libxine-dev libxine1-bin\
    libunicap2 libunicap2-dev swig libv4l-0 libv4l-dev python-numpy\
    libpython2.6 python-dev python2.6-dev libgtk2.0-dev

	
	
-Paso 3: Después de que las bibliotecas hayan terminado de instalar, se descarga la versión de \ac{OpenCV} 2.4.9 utilizando el comando \textit{wget}. 

    pi@raspberrypi $ wget -O openCV-2.4.9.zip http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.9/opencv-2.4.9.zip/download

		
-Paso 4: Finalizada la descarga se tendrá openCV-2.4.9.zip, el paso siguiente es utilizar el comando \textit{unzip} para descomprimir el archivo zip.

    pi@raspberrypi $ unzip openCV-2.4.9.zip 

	
-Paso 5: Esto creará una carpeta \ac{OpenCV}-2.4.9 y además se crea la carpeta \textit{release} que es donde vamos a compilar \ac{OpenCV}.

    pi@raspberrypi $ cd openCV-2.4.9
    pi@raspberrypi /openCV-2.4.9 $ mkdir release
    pi@raspberrypi /openCV-2.4.9 $ cd release


Paso 6: Luego es el momento de configurar \ac{OpenCV}. Se trata de una larga lista, la cual se puede configurar o usar como viene por defecto. Para entrar al menú de configuración escribimos lo siguiente.

    pi@raspberrypi /openCV-2.4.9/release $ sudo ccmake ../ 

-Paso 7:Una vez terminada la configuración y guardada se comienza a ejecutar el siguiente comando: 

    pi@raspberrypi $ make
    pi@raspberrypi $ sudo make install


En este punto se ha terminado exitosamente de instalar \ac{OpenCV}. 
    
    
##Implementación de la detección de caras: Viola \& Jones
    
Dado lo anterior, no caben dudas que este tópico es prioritario para el éxito del proyecto, es por eso que se ha escogido un detector caracterizado por la rapidez en la detección de objetos en una imagen, un alto índice de aciertos y bajo porcentaje de falsos positivos tal como lo es Viola \& Jones.
La implementación se llevó a cabo en SimpleCV. El código es una elaboración conjunta con Sebastián Godoy (profesor guía de esta memoria de título) tomando como base el código disponible en el libro ``Practical Computer Vision with SimpleCV" \cite{PracticalComputerVision} en la sección \textit{Haar-like Features}.


    import SimpleCV                 #Importa funciones de SimpleCV
    from wand.image import Image    #Importa de Image la funcion de MagickWand
    cam = SimpleCV.Camera()	#apertura software de la camara para trabajar con SimpleCV
    count = 1               #Inicializacion de variable
    while count<6:             
    img = cam.getImage()    #Se toma una imagen de la camara
    faces = img.findHaarFeatures('face.xml') #Busqueda caracteristicas Haar
    if faces is not None:            
    faces = faces.sortArea()
    bigFace = faces[-1]              #Se obtiene la cara mas grande
    bigFace.draw()                   #Se dibuja el rectangulo verde
    x,y,w,h = bigFace.boundingBox()  #Devuelve esquinas del rectangulo
    cara = img.crop(x,y,w,h)         #Recortamos la imagen
    cara = cara.resize(220,233)      #Redimensionamos
    cara.save('cara' + str(count) + '.png')  #Guadamos la cara en formato PNG
    with Image(filename='cara' + str(count) + '.png') as OriginalImagen:
    OriginalImagen.format = 'gif'
    OriginalImagen.save(filename='caraGIF' + str(count) + '.gif')   
    count = count + 1       #Aumentamos el contador y se repite el ciclo
    img.show()                          


Para su utilización es necesario instalar \textit{MagickWand} con los siguientes comandos:

    pi@raspberrypi $ apt-get install libmagickwand-dev 
    pi@raspberrypi $ pip install Wand

Lo que hace el programa  es detectar todas las caras presentes en una secuencia de imágenes y guardarlas en formato \texttt{.png} y \texttt{.gif} en el directorio en donde se encuentra guardado el programa, con un tamaño de $220 \times 233$ pixeles.



##Implementación algoritmo de Eigenface
La implementación de Eigenface es muy usada tanto en la industria como en la academia. Se usó una implementación escrita en \textit{Python} con licencia \ac{MIT} donde todo el código se puede descargar de \textit{Google Code} en \url{https://code.google.com/archive/p/pyfaces/} o el repositorio de GitHub \cite{GitHubSeguel}. Lo que se necesita es tener instalado \ac{PIL} lo cual se hizo previamente en la instalación de SimpleCV y \ac{OpenCV}.\\ %sudo apt-get install python-dev python-setuptools
Antes de hacer cualquier cosa lo que necesitamos es hacer un preprocesamiento de la base de datos con el fin de mejorar la eficiencia del algoritmo. 
Entonces, pensando en los futuros lectores de este trabajo se comenzará desde cero. La implementación de este algoritmo está hecho originalmente con la base de datos de \textit{UCSD Computer Vision} llamada \textit{Yale Face Database} la cual contiene 15 individuos con 11 imágenes por sujeto, con imágenes de tamaño de $320 \times 243$ pixeles. Esta base de datos representa la inspiración en los parámetros usados en la creación de la base de datos de elaboración propia.\\
Dadas las acotaciones anteriores se elaborará un preprocesamiento de la base de datos \textit{Yale Face} para posteriormente hacerlo con la base de datos propia. \\
En \textit{Yale Face} todas las imágenes se bajan en un solo directorio. Lo que se necesita es separar por carpetas los individuos para lo cual se siguen los siguientes comandos:

    pi@raspberrypi /yalefaces $ mkdir s01
    pi@raspberrypi /yalefaces $ cp subject01* ./s01


Con esto copiamos todos los archivos que comienzan con \textit{subject01} en la carpeta \textit{s01}.\\
Esto se hace con los siguientes sujetos de igual forma. %en donde se puede crear un \textit{bucle} para hacer la tarea de forma más rápida.
Por otro lado la base de datos \textit{Yale Face} no trae las caras realmente centradas por lo que hay que cortarlas.
\begin{figure}[H]
	\centering
	\includegraphics[scale=0.3]{Figuras/YaleCrop.png}
	\label{Fig:YaleCrop}
	\caption{Ejemplo de imagen de base de datos \textit{Yale Face} que necesita ser recortada.}
\end{figure}
Esto se resuelve con los siguientes comandos:
\begin{lstlisting}[style=bash,label={code:mkdirBaseDatos}]
pi@raspberrypi /yalefaces$ cd s01
pi@raspberrypi /yalefaces$ convert 'subject01*' -crop 320x243+100-10 crop_subject%01d.gif
\end{lstlisting}

Esto recorta todas las imágenes dejando la cara más centrada a $230 \times 233$ \textit{pixeles} y las renombra en formato \textit{gif}. Esto se repite para todos los sujetos. Se recomienda crear un pequeño \textit{script} con un bucle para agilizar ambos procesos.

\begin{figure}[H]
	\centering
	\includegraphics[scale=0.47]{Figuras/ImplementaEigenface01.png}
	\hspace{1cm}
	\includegraphics[scale=0.435]{Figuras/ImplementaEigenface02.png}
	\label{Fig:ImplementaEigenface01}
	\caption{Resultados del prepocesamiento a base de datos \textit{Yale Face}.}
\end{figure}
 
El mismo preprocesamiento se hace con una base de datos propia, ordenar por carpetas los sujetos y recortar en caso de que no estén centradas las imágenes para aumentar eficiencia del algoritmo de reconocimiento facial. Posteriormente se debe dividir las imágenes de los sujetos en conjuntos de entrenamiento y de prueba. En este caso se va a usar una relación de imágenes de entrenamiento y prueba de $8:1$. Para lograr esto se sigue lo siguiente:

\begin{itemize}
	\item Se copian manualmente 8 imágenes de un sujeto en el directorio \textit{pyfaces/gallery} 
	\item Se selecciona la imagen sobrante del sujeto que se someterá a reconocimiento y se copia en el directorio \textit{pyfaces/probes} 
\end{itemize}

\begin{figure}[H]
	\centering
	\label{Fig:PreprocesamientoEigenFaces01}
	\subfigure[Carpetas imágenes preprocesadas.]{\includegraphics[scale=0.5]{Figuras/PreprocesamientoEigenFaces01.png}}\\
	\subfigure[Conjunto de imágenes de prueba \textit{Eigenfaces}.]{\includegraphics[scale=0.48]{Figuras/PreprocesamientoEigenFaces03.png}}
	\subfigure[Conjunto de imágenes de entrenamiento \textit{Eigenfaces}.]{\includegraphics[scale=0.48]{Figuras/PreprocesamientoEigenFaces02.png}}
\end{figure}

Se eligió la relación conjunto de entrenamiento a prueba de forma arbitraria pudiendo escoger cualquier otra relación y observar sus resultados.\\
Se puede ver que las imágenes de prueba corresponden a todas las expresiones normales de los sujetos y estas no se encuentran en la carpeta de imágenes de entrenamiento que contiene las restantes expresiones.\\
De esta manera ya se puede ejecutar el código %el cual ya trae un manual con un archivo en el directorio \textit{/EigenFaces/pyfaces/pyfacescmd} el cual se llama \textit{usage.txt}, lo cual %
de la siguiente manera. 

\begin{lstlisting}[style=bash,label={code:RunEigenFaces}]
pi@raspberrypi .../pyfaces/pyfacescmd $ python pyfacesdemo ImagenPrueba  BasedeDatos NumerodeEigenFaces Threshold
 \end{lstlisting}
 %python pyfacesdemo /home/pi/Desktop/CodigosMT/EigenFaces/pyfaces/pyfaces/probes/s01Normal7.gif /home/pi/Desktop/CodigosMT/EigenFaces/pyfaces/pyfaces/gallery/ 15 3

Donde los parámetros que se pasan a programa en \textit{Python} representan:

\begin{description}
	\item[ImagenPrueba]: Directorio donde se encuentra la imagen de prueba (Ejemplo: \textit{/home/pi/.../pyfaces/probes/s01Normal7.gif})
	\item[BasedeDatos]: Directorio donde se encuentra la galería completa de la base de datos (Ejemplo: \textit{/home/pi/.../pyfaces/gallery/})
	\item[NumerodeEigenFaces]:Número de \textit{Eigenfaces} que se necesitan.
	\item[Threshold]: Umbral máximo admisible de distancia Euclidiana. Si se sobrepasa sujeto no se encuentra en base de datos.
\end{description}

Como acotación necesariamente las imágenes de prueba y de entrenamiento tienen que tener el mismo formato y en promedio exigimos a la Raspberry Pi al $25\%$ de su capacidad de procesamiento. \\
El resultado del procesamiento entrega lo siguiente:
\begin{lstlisting}[style=bash,label={code:ResultadoEigen}]
pi@raspberrypi /Desktop/ ... /pyfaces/pyfacescmd $ python pyfacesdemo/ ../pyfaces/probes/s01Normal7.gif ../pyfaces/gallery/ 15\ 2
Imagen de Prueba: ../pyfaces/probes/s01Normal7.gif  para imagenes extension gif en Base de Datos: ../pyfaces/gallery/
numero de eigenfaces utilizadas: 15
no hay archivo cache(algoritmo no entrenado)
probando reconstruccion
Elaborando directorio: ../reconfaces
matches :../pyfaces/gallery/s01Feliz1.gif dist :0.123344144392
tiempo ejecucion : 284.600765944 secs
\end{lstlisting}

%\begin{figure}[H]
%	\centering
%	\includegraphics[scale=0.7]{Figuras/ResultadosEigenfaces.png}
%	\label{Fig:ResultadosEigenfaces}
%\end{figure}

En el ejemplo entrega como resultado de reconocimiento la imagen \textit{s01Feliz1.gif} para la imagen de prueba \textit{s01Normal7.gif} que no se encuentra en la base de datos y resulta ser correcto. Es que mencionar que el tiempo de ejecución aproximadamente de $4.7$ min. Si bien es alto y se aleja de una aplicación en tiempo real este baja considerablemente una vez que el algoritmo ya se entrena aproximadamente a $65$ seg.. \\
Por otra parte, en forma de resultados esta implementación crea dos carpetas que contienen todas las \textit{Eigenfaces} calculadas y otra carpeta con caras reconstruidas, en donde la implementación trata de reconstruir las caras dado el número de \textit{Eigenfaces} que se da como parámetro. Además entrega la cara promedio que para el ejemplo es la siguiente:\\

\begin{figure}[H]
	\centering
	\includegraphics[scale=0.7]{Figuras/CaraPromedioEigenFaces.png}
	\label{Fig:CaraPromedioEigenFaces}
	\caption{Cálculo de la cara promedio.}
\end{figure}
\begin{figure}[H]
	\centering
	\subfigure[Algunas \textit{Eigenfaces} calculadas.]{\includegraphics[scale=0.55]{Figuras/ResultadosEigenfaces01.png}}
	\subfigure[Caras reconstruidas.]{\includegraphics[scale=0.55]{Figuras/ResultadosEigenfaces02.png}}
	\label{Fig:ResultadosEigenfaces02}
\end{figure}
Otra forma de usar esta implementación del algoritmo \textit{Eigenfaces} es mediante interfaz gráfica que funciona de igual manera. Es que tener la precaución de volver a entrenar el algoritmo, para ello se eliminan las carpetas $eigenfaces$ y $reconfaces$ y el $saveddate.cache$ que se crea en la carpeta $gallery$ que corresponde a la base de datos.
Además necesita el paquete \textit{Tix} el cual se instala con:
\begin{lstlisting}[style=bash,label={code:Tix}]
pi@raspberrypi $ sudo apt-get install tix-dev
\end{lstlisting}

\begin{figure}[H]
	\centering
	\includegraphics[scale=0.6]{Figuras/InterfazEigenfaces.png}
	\label{Fig:InterfazEigenfaces}
	\caption{Interfaz gráfica para reconocimiento de rostros usando \textit{Eigenfaces}}
\end{figure}

La guía completa de esta implementación la cual sirvió para comentar en detalle esta implementación corresponde a Sajan \cite{ImplementacionAlgoritmoEigenfaces} con su artículo \textit{Face Recognition in Python}.

\newpage
\subsection[]{Implementación método de clasificación ocupando distancia Euclidiana}

La implementación de este método de clasificación se llevo a cabo ocupando \textit{SciPy} que es una biblioteca de código abierto el cual contiene algoritmos y herramientas para \textit{Python} que permite hacer el procesamiento de imágenes. Esta librería se encuentra orientada al mismo tipo de usuarios de aplicaciones como \textit{Matlab}. 

\begin{figure}[H]
	\centering 
	\subfigure[NumPy, Biblioteca SciPy y Matplotlib]{\includegraphics[scale=0.5]{Figuras/NumPy.png}}
	\label{Fig:LibreriasParaDistEuclidiana}
\end{figure}


La implementación lo que hace es comparar el parecido entre dos caras. Para eso calcula la distancia Euclidiana entre la imagen que se quiere reconocer y un conjunto de imágenes de entrenamiento que se obtienen de la implementación de \textit{Eigenface} y es el cálculo de la cara promedio de cada sujeto. Luego busca un mínimo entre todas esas distancias de las cuales cálculo, desplegando la imagen que reconoció con su correspondiente distancia Euclianana y la normalización del número de pixeles.


\begin{figure}[H]
	\centering
	\subfigure[Imagen a reconocer por el método]{\includegraphics[scale=0.42 ]{Figuras/DEImagenAReconocer.png}}\hspace{1.5cm}
	\subfigure[Imagen reconocida por el método de clasificación distancia Euclidiana ]{\includegraphics[scale=0.42]{Figuras/DEReconocida.png}}
	\label{fig:Figuras2y3DE}
\end{figure}
	


\begin{figure}[H]
	\centering
	\includegraphics[scale=0.6]{Figuras/DEConjuntoEntrenamiento.png}
	\label{Fig: ConjuntoEntrenamiento}
	\caption{Conjunto de Entrenamiento para método Distancia Euclidiana}
\end{figure}

La implementación parece bastante básica, y no se ejecuta en tiempo real como se había pensado en un principio pero busca demostrar que este método de clasificación es el peor y da los peores resultados de reconocimiento.
\newpage
\subsection[]{Implementación método de clasificación \acf{SVM}}

La implementación de este algoritmo es capaz de detectar rostros mediante clasificadores en cascada basados en la función de \textit{Haar} propuestos por el método de detección de objetos de Paul Viola \& Michael Jones \cite{OpenCVHaarCascade}. La implementación utilizada fue creada por Chenxing Ouyang \cite{SVMHaarCascade} la cual posee una  mejora al método de Viola \& Jones que permite la detección hasta en $45^{\circ}$ grados de inclinación de la cabeza. Por lo tanto la implementación es un sistema práctico para el seguimiento y reconocimientos de rostros en tiempo real. \\

El diseño del sistema consta específicamente de los siguientes pasos:
\begin{itemize}
	\item \textbf{Pre-procesado de la imagen:} Esto implica cambiar el tamaño y rotar cada cuadro del flujo de vídeo.
	\item \textbf{Detección de rostro:} Usando la función \textit{Haar} como clasificador en cascada.
	\item \textbf{Preparación de base de datos:} Esto implica recortar la imagen, cambiar el tamaño y ponerla en escala de grises.
	\item \textbf{Se calculan las \emph{Eigenfaces}:} Se extraen características y se seleccionan las mejores.
	\item \textbf{Clasificación:} Se ocupa el método de clasificación de \ac{SVM} con un \textit{kernel} \ac{RBF}, tangente hiperbólica (sigmoid), lineal (linear) y polinomial (poly).
	\item \textbf{Resultados de clasificación:} Se exponen en tiempo real.
\end{itemize}
La detección y reconocimiento de la cara fueron implementados en \textit{Python}. En una primera etapa esta implementación detecta si existe frente a la cámara algún rostro utilizando clasificadores entrenados que vienen en \ac{OpenCV}. Este tipo de clasificadores se basan en características \textit{Haar} que evalúan apariencia, es decir una combinación de características tales como color de la piel y la forma de la cabeza. Para lograr esto se comparan y calculan los \textit{frames} obtenidos del flujo de imágenes de la Pi-cam. Una ventaja de usar este método usando \ac{SVM} es su aprendizaje automático debido al entrenamiento de una cantidad de imágenes positivas y negativas. Una vez entrenado el sistema de detección de caras se procesa rápido y eficazmente \cite{SVMHaarCascade}.\\
 %Para poner en ejecución este método en tiempo real, el algoritmo de detección se ejecuta en cada frame del proceso. \\
En \ac{OpenCV}, las características \textit{Haar} vienen escritas con parámetros de optimización, tales como distancias mínimas entre caras para la detección de caras múltiples y los tamaños mínimo de cara a ser detectados, entre otros \cite{SVMHaarCascade}. %A lo largo de el estudio ya sea de detección y reconocimiento se aprecia un denominador común que es que la cabeza ocupa un pequeño espacio dentro de una imagen.% lo que hace genera una manera extraña de mirar a las personas en la vida real.\\ 
Las características \textit{Haar} finalmente en código no son más que largos archivos XML de aproximadamente 30 mil líneas de código.


\begin{figure}[H]
	\centering
	\includegraphics[scale=0.8]{Figuras/ClassifiSVMImp.png}
	\caption{Ejemplos de características \textit{Haar} en código XML}
	\label{Fig:ClassifiSVMImp}
\end{figure}

Este tipo de archivos con nombre como \textit{``haarcascade\_frontalface\_alt\_tree.xml"} o nombres similares son los clasificadores que se pueden elegir y son de código abierto. Están muy afinados para los perfiles que se necesitan detectar y lo que contienen son umbrales que se puede ver a continuación:% donde hay una cantidad de umbrales.
 
\begin{lstlisting}[style=xml,caption={Pequeña parte de código XML de haarcascada frontalface.},label={code:haarcascade_frantalface}]
<maxWeakCount>9</maxWeakCount>
<stageThreshold>-1.6378560066223145e+00</stageThreshold>
<weakClassifiers>
<_>
<internalNodes>
0 -1 3 8.7510552257299423e-03</internalNodes>
<leafValues>
-8.5947072505950928e-01 3.6881381273269653e-01</leafValues></_>
\end{lstlisting}

Por otro lado una mejora de procesamiento hecha por Ouyang,  fue cambiar el tamaño de la imagen a procesar a una cuarta parte y pasarla a escala de grises antes de ser procesadas por el sistema de detección de rostros \cite{SVMHaarCascade}. Una vez que se encuentre una cara esta se recorta y se introducen al sistema de reconocimiento facial.
\begin{figure}[H]
	\centering
	\subfigure{\includegraphics[scale=0.97]{Figuras/ResultadoImplSVM1.png}}
	\subfigure{\includegraphics[scale=0.64]{Figuras/ResultadoImplSVM2.png}}
	\caption{Cara recortada después de ser detectada por el sistema.}
	\label{Fig:CaradelsistemaSVM}
\end{figure}

Tal como se menciona una limitación del algoritmo original propuesto por Viola \& Jones es detectar caras giradas, lo cual se soluciona con la implementación de su propio algoritmo de detección de rostros girados elaborada por el autor, lo cual se basa en la suposición de que la gente normalmente inclina más o menos $45^{\circ}$ grados ya sea para la izquierda o derecha la cabeza. La implementación se basa en un mapeo realizado con librerías de \textit{Python} apoyándose en el hecho de que los clasificadores en cascada pueden hacer hasta $15^{\circ}$ de giro ya sea a izquierda o derecha. Entonces se examina en tiempo real cada \textit{frame} tres rotaciones (izquierda, medio, derecha) a través de una trasformación geométrica permitiendo la detección del rostro usando la función de \ac{OpenCV} para \textit{Python} \textit{getRotationMatrix2D} \cite{OpenCvTransforGeometrica} que recibe los parámetros:%(w/2, h/2), rotation, scale)

\begin{itemize}
	\item \textbf{center:} Es el centro de la imagen a la que se quiere hacer la rotación.
	\item \textbf{angle:} Es el ángulo de rotación en grados. Los valores positivos significan rotación en sentido antihorario.
	\item \textbf{scale:} Factor de escala isotrópica de la imagen girada.
	\item \textbf{mapMatrix:} La transformación afín de salida, la matriz de punto flotante 2x3.
\end{itemize}

La función calcula la matriz:
	\[ \left( \begin{array}{ccc}
	\alpha & \beta & (1-\alpha)\cdot \text{center}_{.}x-\beta\cdot \text{center}_{.}y \\
	-\beta & \alpha & \beta\cdot \text{center}_{.}x+(1-\alpha)\cdot \text{center}_{.}y \end{array} \right)\] 
donde 
\begin{equation*}
	\alpha = \text{scale}\cdot cos \hspace{0.1cm} \text{angle}\\
\end{equation*}
\begin{equation*}
\beta = \text{scale}\cdot sin \hspace{0.1cm}\text{angle}
\end{equation*}

Se recomienda al lector ver el código utils.py la función \textit{rotate\_image} que se encuentra disponible en el repositorio de la implementación en \textit{GitHub} \cite{GitHubSeguel} para ahondar más sobre la implementación realizada. Esto logra una detección de hasta $45^{\circ}$ grados de inclinación de la cabeza, como se muestra en la figura \ref{Fig:RotacionCentro} a continuación:
\begin{figure}[H]
	\centering
	\subfigure[Inclinación izquierda $45^{\circ}$ grados.]{\includegraphics[scale=0.8]{Figuras/RotacionIzq02.png}}
	\subfigure[Inclinación de 0 grados]{\includegraphics[scale=0.8]{Figuras/RotacionCentro02.png}}
	\subfigure[Inclinación derecha $45^{\circ}$ grados]{\includegraphics[scale=0.8]{Figuras/RotacionDer02.png}}
	\caption{Rotación de la cara para sistema de detección de rostro.}
	\label{Fig:RotacionCentro}
\end{figure}

Para lograr estos resultados primero se necesito:
\begin{description}
\item[Preparación de base de datos:] La base de datos usada fue de creación propia. Las imágenes recortadas son originalmente de $192 \times 172$ pixeles, las cuales se re-dimensionan a $50 \times 50$ pixeles con el fin, de lograr una mayor velocidad de procesamiento durante el entrenamiento y la detección. Además la implementación trae consigo un sistema que permite a los usuarios de forma automática tomar fotografías a usuarios tan solo especificando un directorio para guardar el perfil guardando imágenes de entrenamiento en tiempo real \cite{SVMHaarCascade} usando el programa:
\begin{lstlisting}[style=bash,label={code:SVMTrain}]
pi@raspberrypi /Desktop/ ... /scripts $ python train.py [face_profile_name=<Nombre de carpeta perfil del sujeto>]

\end{lstlisting}
	
	
\item[Extracción de caracteristicas:] Tomando las imágenes de la base de datos se forman dos conjuntos uno de entrenamiento y de prueba en una proporción $3:1$ al azar. Con esto se extraen las caracteristicas más representativas en forma de valores numéricos los cuales se comparan y evalúan posteriormente. En este caso se trabajo con las mejores $6$ variando hasta $54$ \textit{Eigenfaces} en vez  de las $150$ que propuso el autor de la implementación para comparar de forma justa con el algoritmo que ocupa solo \textit{Eigenfaces} y distancia euclidiana para el reconocimiento de rostros.

\item[Clasificación] Con la utilización del modelo estadístico de \ac{SVM} se separan conjuntos de datos, con el fin de tener distancias máximas entre datos de diferentes clases. El código fue implementado usando \textit{scikit-learn} en donde \ac{PCA}, específicamente \textit{Eigenfaces} alimenta el modelo de clasificación \cite{SVMHaarCascade}.
	
\end{description}


Finalmente, la aplicación se utiliza en tiempo real, corriendo a 10 \textit{frames} por segundo con una alta precisión en el reconocimiento lo cual es relativo al número de imágenes de entrenamiento y la tan representativas sean esas imágenes en el conjunto de entrenamiento.

 
