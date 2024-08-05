# -*- coding: utf-8 -*-
"""
Created on Wed May 10 20:25:44 2023

@author: Usuario
"""

import cv2
import numpy as np


img=cv2.imread("C:\\Users\\Usuario\\Desktop\\mano.jpg",cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2=cv2.imread("C:\\Users\\Usuario\\Desktop\\mano.jpg",cv2.IMREAD_COLOR)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

kernel=np.array([[0,1,0],[1,-4,1],[0,1,0]])

img2=cv2.filter2D(img,0,kernel)

cv2.imshow('Original', img)
cv2.imshow('Filtro', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

