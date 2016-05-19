# CodigosMT
Se presentan todos los codigos desarrollados y modificados del Trabajo de Memoria de título Detección de Rostros en tiempo real usando plataforma Raspberry Pi para obtar a título de Ingeniero Civil en Telecomunicaciones

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

-Encender la Raspberry Pi e ingresar:
    $ cd nombreRepositorio
    nombreRepositorio/$ git config -l
    pi@raspberrypi ~$ Username: pi
    pi@raspberrypi ~$ Password:
   
- Conectar la tarjeta a internet.
- Instalar las bibliotecas obligatorias ejecutando el siguiente comando para instalar las dependencias

    pi@raspberrypi ~$ sudo pip install https://github.com/sightmachine/SimpleCV/zipball/master
    
    
 
