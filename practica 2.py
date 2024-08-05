# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:54:47 2023

@author: Usuario
"""

import numpy as np
import cv2
#Estas librerias son para trabajar con matrices

img = cv2.imread(r"C:\Users\Usuario\Downloads\hands.jpg", cv2.IMREAD_COLOR)
img_64 = np.asarray(img,dtype=np.float64)

fila = img.shape [0]

columna = img.shape[1]

color = 3

imgcrom = np.zeros([fila,columna,color])

#img oscura 1

dark = img[:,:,:]*(0.5) 

dark8 = np.asarray(dark,dtype=np.float64)

darkcrom = np.zeros([fila,columna,color])

#img oscura 2

dark2 = img[:,:,:]*(0.5) 

dark82 = np.asarray(dark2,dtype=np.float64)

darkcrom2 = np.zeros([fila,columna,color])

#maximos y minimos foto original 

imgmx = np.array [206,228,254]
imgmn = np.array [56,79,118]


difimgosc = np.array [fila, columna]
difcromosc = np.array [fila, columna]
difcromosc2 = np.array [fila, columna]

#cromatiza

def cromatico (cromatica, base)
for x in range (fila) :
    
    for y in range (columna):
        
        for c in range (color):
            
            imgcorr [x,y] = ( img[x,y,c] / (img[x,y,0] + img [x,y,1] + img [x,y,2])
        








cv2.imshow('foto',img)

cv2.imshow('bn',imgcorr)

cv2.waitKey(0)