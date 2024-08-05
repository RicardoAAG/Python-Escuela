# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:33:44 2023

@author: super
"""

import cv2
import numpy as np


img=cv2.imread("C:\\Users\\Usuario.DESKTOP-L133VTH\\Desktop\\manos.jpg",cv2.IMREAD_COLOR)
filas=img.shape[0]
columnas=img.shape[1]
bn=np.zeros([filas,columnas])

maxi=np.array([205,216,241],np.uint8)
mini=np.array([49,71,153],np.uint8)

"""bn=cv2.inRange(img,mini,maxi)"""

for i in range(filas):
    for j in range(columnas):      
            if(mini[0]<=img[i,j,0]<=maxi[0]):
                if(mini[1]<=img[i,j,1]<=maxi[1]):
                    if(mini[2]<=img[i,j,2]<=maxi[2]):
                        bn[i,j]=255



cv2.imshow("imagen",img)
cv2.imshow("blanco y negro",bn)


cv2.waitKey(0)
cv2.destroyAllWindows()