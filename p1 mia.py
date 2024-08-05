# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:44:59 2023

@author: Usuario
"""

import numpy as np
import cv2
#Estas librerias son para trabajar con matrices

img = cv2.imread(r"C:\Users\Usuario\Downloads\mano.jpg", cv2.IMREAD_COLOR)

imgbn = np.zeros((img.shape[0], img.shape[1] ) )

for x in range (img.shape[0] ):
    
    for y in range (img.shape[1] ) :
        
        if ( (56 < img[x,y,0] < 206 ) and (79 < img[x,y,1] <228 ) and (118 < img [x,y,2]< 254)  ) :
        
         imgbn [x,y] = 1;

cv2.imshow('foto',img)

cv2.imshow('bn',imgbn)

cv2.waitKey(0)