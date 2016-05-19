import cv2
import os
import numpy as np
from scipy import ndimage
from time import time
import sys
import logging
import warnings
import warnings
import commands
import matplotlib.pyplot as plt



with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from sklearn.cross_validation import train_test_split


#face_profile_data, face_profile_name_index, face_profile_names  = ut.load_training_data("../face_profiles/")
#X = face_profile_data
#y = face_profile_name_index
#print "face_profile_data=",face_profile_data
#print "\v"
#print "face_profile_name_index=",face_profile_name_index
#print "\v"
#print "face_profile_names=",face_profile_names
#print "\v"

# MODO 1 SEPARADA

# Myface_profile_datas01= ['s01Durmiendo', 's01Feliz', 's01Guino', 's01LuzCentral', 's01LuzDerecha', 's01LuzIzquierda', 's01Normal', 's01Sorpresa', 's01Triste']
# Myface_profile_datas02= ['s02Durmiendo', 's02Feliz', 's02Guino', 's02LuzCentral', 's02LuzDerecha', 's02LuzIzquierda', 's02Normal', 's02Sorpresa', 's02Triste']
# Myface_profile_datas03= ['s03Durmiendo', 's03Feliz', 's03Guino', 's03LuzCentral', 's03LuzDerecha', 's03LuzIzquierda', 's03Normal', 's03Sorpresa', 's03Triste']
# Myface_profile_datas04= ['s04Durmiendo', 's04Feliz', 's04Guino', 's04LuzCentral', 's04LuzDerecha', 's04LuzIzquierda', 's04Normal', 's04Sorpresa', 's04Triste']
# Myface_profile_datas05= ['s05Durmiendo', 's05Feliz', 's05Guino', 's05LuzCentral', 's05LuzDerecha', 's05LuzIzquierda', 's05Normal', 's05Sorpresa', 's05Triste']
# Myface_profile_datas06= ['s06Durmiendo','s06Feliz', 's06Guino', 's06LuzCentral', 's06LuzDerecha', 's06LuzIzquierda', 's06Normal', 's06Sorpresa', 's06Triste']
# Myface_profile_datas07= ['s07Durmiendo', 's07Feliz','s07Guino', 's07LuzCentral', 's07LuzDerecha', 's07LuzIzquierda', 's07Normal', 's07Sorpresa', 's07Triste']
# Myface_profile_datas08= ['s08Durmiendo', 's08Feliz', 's08Guino', 's08LuzCentral', 's08LuzDerecha', 's08LuzIzquierda', 's08Normal', 's08Sorpresa', 's08Triste']
# Myface_profile_datas09= ['s09Durmiendo', 's09Feliz', 's09Guino', 's09LuzCentral', 's09LuzDerecha', 's09LuzIzquierda', 's09Normal', 's09Sorpresa', 's09Triste']
# Myface_profile_datas10= ['s10Durmiendo', 's10Feliz', 's10Guino', 's10LuzCentral', 's10LuzDerecha', 's10LuzIzquierda', 's10Normal', 's10Sorpresa', 's10Triste']
# Myface_profile_datas11= ['s11Durmiendo', 's11Feliz', 's11Guino', 's11LuzCentral', 's11LuzDerecha', 's11LuzIzquierda', 's11Normal', 's11Sorpresa', 's11Triste']
# Myface_profile_datas12= ['s12Durmiendo', 's12Feliz', 's12Guino', 's12LuzCentral', 's12LuzDerecha', 's12LuzIzquierda', 's12Normal', 's12Sorpresa', 's12Triste']
# Myface_profile_datas13= ['s13Durmiendo', 's13Feliz', 's13Guino', 's13LuzCentral', 's13LuzDerecha', 's13LuzIzquierda', 's13Normal', 's13Sorpresa', 's13Triste']
# Myface_profile_datas14= ['s14Durmiendo', 's14Feliz', 's14Guino', 's14LuzCentral', 's14LuzDerecha', 's14LuzIzquierda', 's14Normal', 's14Sorpresa', 's14Triste']
# Myface_profile_datas16= ['s16Durmiendo', 's16Feliz', 's16Guino', 's16LuzCentral', 's16LuzDerecha', 's16LuzIzquierda', 's16Normal', 's16Sorpresa', 's16Triste']
# Myface_profile_datas18= ['s18Durmiendo', 's18Feliz', 's18Guino', 's18LuzCentral', 's18LuzDerecha', 's18LuzIzquierda', 's18Normal', 's18Sorpresa', 's18Triste']
# Myface_profile_datas19= ['s19Durmiendo', 's19Feliz', 's19Guino', 's19LuzCentral', 's19LuzDerecha', 's19LuzIzquierda', 's19Normal', 's19Sorpresa', 's19Triste']
# Myface_profile_datas20= ['s20Durmiendo', 's20Feliz', 's20Guino', 's20LuzCentral', 's20LuzDerecha', 's20LuzIzquierda', 's20Normal', 's20Sorpresa', 's20Triste']


# Myface_profile_name_indexs01 = ['s01', 's01', 's01', 's01', 's01', 's01', 's01','s01', 's01']
# Myface_profile_name_indexs02 = ['s02', 's02', 's02', 's02', 's02', 's02', 's02','s02', 's02']
# Myface_profile_name_indexs03 = ['s03', 's03', 's03', 's03', 's03', 's03', 's03','s03', 's03']
# Myface_profile_name_indexs04 = ['s04', 's04', 's04', 's04', 's04', 's04', 's04','s04', 's04']
# Myface_profile_name_indexs05 = ['s05', 's05', 's05', 's05', 's05', 's05', 's05','s05', 's05']
# Myface_profile_name_indexs06 = ['s06', 's06', 's06', 's06', 's06', 's06', 's06','s06', 's06']
# Myface_profile_name_indexs07 = ['s07', 's07', 's07', 's07', 's07', 's07', 's07','s07', 's07']
# Myface_profile_name_indexs08 = ['s08', 's08', 's08', 's08', 's08', 's08', 's08','s08', 's08']
# Myface_profile_name_indexs09 = ['s09', 's09', 's09', 's09', 's09', 's09', 's09','s09', 's09']
# Myface_profile_name_indexs10 = ['s10', 's10', 's10', 's10', 's10', 's10', 's10','s10', 's10']
# Myface_profile_name_indexs11 = ['s11', 's11', 's11', 's11', 's11', 's11', 's11','s11', 's11']
# Myface_profile_name_indexs12 = ['s12', 's12', 's12', 's12', 's12', 's12', 's12','s12', 's12']
# Myface_profile_name_indexs13 = ['s13', 's13', 's13', 's13', 's13', 's13', 's13','s13', 's13']
# Myface_profile_name_indexs14 = ['s14', 's14', 's14', 's14', 's14', 's14', 's14','s14', 's14']
# Myface_profile_name_indexs16 = ['s16', 's16', 's16', 's16', 's16', 's16', 's16','s16', 's16']
# Myface_profile_name_indexs18 = ['s18', 's18', 's18', 's18', 's18', 's18', 's18','s18', 's18']
# Myface_profile_name_indexs19 = ['s19', 's19', 's19', 's19', 's19', 's19', 's19','s19', 's19']
# Myface_profile_name_indexs20 = ['s20', 's20', 's20', 's20', 's20', 's20', 's20','s20', 's20']


# X_train, X_test, y_train, y_test = train_test_split(Myface_profile_datas16, Myface_profile_name_indexs16, test_size=0.25, random_state=42) #Validacion cruzada
# print "X_train=",X_train 
# print "\v"
# print "X_test=",X_test
# print "\v"
# print "y_train=",y_train
# print "\v"
# print "y_test=",y_test
# print "\v"

# Modo 2 JUNTA

Myface_profile_datas= ['s01Durmiendo', 's01Feliz', 's01Guino', 's01LuzCentral', 's01LuzDerecha', 's01LuzIzquierda', 's01Normal', 's01Sorpresa', 's01Triste','s02Durmiendo', 's02Feliz', 's02Guino', 's02LuzCentral', 's02LuzDerecha', 's02LuzIzquierda', 's02Normal', 's02Sorpresa', 's02Triste','s03Durmiendo', 's03Feliz', 's03Guino', 's03LuzCentral', 's03LuzDerecha', 's03LuzIzquierda', 's03Normal', 's03Sorpresa', 's03Triste','s04Durmiendo', 's04Feliz', 's04Guino', 's04LuzCentral', 's04LuzDerecha', 's04LuzIzquierda', 's04Normal', 's04Sorpresa', 's04Triste','s05Durmiendo', 's05Feliz', 's05Guino', 's05LuzCentral', 's05LuzDerecha', 's05LuzIzquierda', 's05Normal', 's05Sorpresa', 's05Triste','s06Durmiendo','s06Feliz', 's06Guino', 's06LuzCentral', 's06LuzDerecha', 's06LuzIzquierda', 's06Normal', 's06Sorpresa', 's06Triste','s07Durmiendo', 's07Feliz','s07Guino', 's07LuzCentral', 's07LuzDerecha', 's07LuzIzquierda', 's07Normal', 's07Sorpresa', 's07Triste','s08Durmiendo', 's08Feliz', 's08Guino', 's08LuzCentral', 's08LuzDerecha', 's08LuzIzquierda', 's08Normal', 's08Sorpresa', 's08Triste','s09Durmiendo', 's09Feliz', 's09Guino', 's09LuzCentral', 's09LuzDerecha', 's09LuzIzquierda', 's09Normal', 's09Sorpresa', 's09Triste','s10Durmiendo', 's10Feliz', 's10Guino', 's10LuzCentral', 's10LuzDerecha', 's10LuzIzquierda', 's10Normal', 's10Sorpresa', 's10Triste','s11Durmiendo', 's11Feliz', 's11Guino', 's11LuzCentral', 's11LuzDerecha', 's11LuzIzquierda', 's11Normal', 's11Sorpresa', 's11Triste','s12Durmiendo', 's12Feliz', 's12Guino', 's12LuzCentral', 's12LuzDerecha', 's12LuzIzquierda', 's12Normal', 's12Sorpresa', 's12Triste','s13Durmiendo', 's13Feliz', 's13Guino', 's13LuzCentral', 's13LuzDerecha', 's13LuzIzquierda', 's13Normal', 's13Sorpresa', 's13Triste','s14Durmiendo', 's14Feliz', 's14Guino', 's14LuzCentral', 's14LuzDerecha', 's14LuzIzquierda', 's14Normal', 's14Sorpresa', 's14Triste','s16Durmiendo', 's16Feliz', 's16Guino', 's16LuzCentral', 's16LuzDerecha', 's16LuzIzquierda', 's16Normal', 's16Sorpresa', 's16Triste','s18Durmiendo', 's18Feliz', 's18Guino', 's18LuzCentral', 's18LuzDerecha', 's18LuzIzquierda', 's18Normal', 's18Sorpresa', 's18Triste','s19Durmiendo', 's19Feliz', 's19Guino', 's19LuzCentral', 's19LuzDerecha', 's19LuzIzquierda', 's19Normal', 's19Sorpresa', 's19Triste','s20Durmiendo', 's20Feliz', 's20Guino', 's20LuzCentral', 's20LuzDerecha', 's20LuzIzquierda', 's20Normal', 's20Sorpresa', 's20Triste']


Myface_profile_name_indexs = ['s01', 's01', 's01', 's01', 's01', 's01', 's01','s01', 's01','s02', 's02', 's02', 's02', 's02', 's02', 's02','s02', 's02','s03', 's03', 's03', 's03', 's03', 's03', 's03','s03', 's03','s04', 's04', 's04', 's04', 's04', 's04', 's04','s04', 's04','s05', 's05', 's05', 's05', 's05', 's05', 's05','s05', 's05','s06', 's06', 's06', 's06', 's06', 's06', 's06','s06', 's06','s07', 's07', 's07', 's07', 's07', 's07', 's07','s07', 's07','s08', 's08', 's08', 's08', 's08', 's08', 's08','s08', 's08','s09', 's09', 's09', 's09', 's09', 's09', 's09','s09', 's09','s10', 's10', 's10', 's10', 's10', 's10', 's10','s10', 's10','s11', 's11', 's11', 's11', 's11', 's11', 's11','s11', 's11','s12', 's12', 's12', 's12', 's12', 's12', 's12','s12', 's12','s13', 's13', 's13', 's13', 's13', 's13', 's13','s13', 's13','s14', 's14', 's14', 's14', 's14', 's14', 's14','s14', 's14','s16', 's16', 's16', 's16', 's16', 's16', 's16','s16', 's16','s18', 's18', 's18', 's18', 's18', 's18', 's18','s18', 's18','s19', 's19', 's19', 's19', 's19', 's19', 's19','s19', 's19','s20', 's20', 's20', 's20', 's20', 's20', 's20','s20', 's20']


X_train, X_test, y_train, y_test = train_test_split(Myface_profile_datas, Myface_profile_name_indexs, test_size=0.25, random_state=42) #Validacion cruzada
print "X_train=",X_train 
print "\v"
print "X_test=",X_test
print "\v"
print "y_train=",y_train
print "\v"
print "y_test=",y_test
print "\v"