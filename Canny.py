# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:06:31 2023

@author: super
"""

import numpy as np
import cv2

#trackbar callback fucntion does nothing but required for trackbar
def nothing(x):
	pass

#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls')
#create trackbar in 'controls' window with name 'r''
cv2.createTrackbar('r','controls',0,1000,nothing)
cv2.createTrackbar('s','controls',0,1000,nothing)

#create a while loop act as refresh for the view 
while(1):
    img = cv2.imread('C:\\Users\\super\\OneDrive\\Escritorio\\cartas.png', cv2.IMREAD_GRAYSCALE)

	#leer los valores de trackbar
    maximo= int(cv2.getTrackbarPos('r','controls'))
    minimo= int(cv2.getTrackbarPos('s','controls'))
    
    #funcion canny
    bordes = cv2.Canny(img,minimo,maximo)
    
    #detectar y dibujar los bordes
    ctns, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, ctns, -1, (0,0,255), 2)
    
    #escribir el texto
    texto = 'Contornos encontrados: '+ str(len(ctns))
    cv2.putText(img, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 0, 0), 1)

    cv2.imshow('imagen',img)  
    cv2.imshow('canny',bordes)
	
	# waitfor the user to press escape and break the while loop 
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()   # cierra toda las ventanas
        break