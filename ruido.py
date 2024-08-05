# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:33:44 2023

@author: super
"""

import cv2
import numpy as np
import random

def sal_pimienta(img,porciento):
    num=int(porciento*img.shape[0]*img.shape[1])# Número de puntos de ruido de sal y pimienta
    random.randint(0, img.shape[0])
    img2=img.copy()
    for i in range(num):
        X=random.randint(0,img2.shape[0]-1)# Un número entero aleatorio desde 0 hasta la longitud de la imagen, porque es un intervalo cerrado, -1
        Y=random.randint(0,img2.shape[1]-1)
        if random.randint(0,1) ==0: # Probabilidad en blanco y negro 50%
            img2[X,Y] = (255,255,255)#blanco
        else:
            img2[X,Y] =(0,0,0)#negro
    return img2

img=cv2.imread("C:\\Users\\Usuario.DESKTOP-L133VTH\\Desktop\\spitfire.jpg",cv2.IMREAD_COLOR)
sp_img=sal_pimienta(img,0.1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filas=img.shape[0]
columnas=img.shape[1]

ruido_gauss=np.zeros((filas,columnas),dtype=np.uint8)
cv2.randn(ruido_gauss,128,30)
ruido_gauss=(ruido_gauss*0.5).astype(np.uint8)
gn_img=cv2.add(img,ruido_gauss)

img2=cv2.imread("C:\\Users\\Usuario.DESKTOP-L133VTH\\Desktop\\ariete.jpg",cv2.IMREAD_COLOR)
sp_img2=sal_pimienta(img2,0.1)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
filas2=img2.shape[0]
columnas2=img2.shape[1]

ruido_gauss2=np.zeros((filas2,columnas2),dtype=np.uint8)
cv2.randn(ruido_gauss2,128,30)
ruido_gauss2=(ruido_gauss2*0.3).astype(np.uint8)
gn_img2=cv2.add(img2,ruido_gauss2)

#se le aplica media
media_gn_img = cv2.blur(gn_img, (3, 3))
media_sp_img = cv2.blur(sp_img, (3, 3))
media_gn_img2 = cv2.blur(gn_img2, (3, 3))
media_sp_img2 = cv2.blur(sp_img2, (3, 3))

#se le aplica filtro gausiano
gaus_gn_img = cv2.GaussianBlur(gn_img,(3,3),0)
gaus_sp_img = cv2.GaussianBlur(sp_img,(3,3),0)
gaus_gn_img2 = cv2.GaussianBlur(gn_img2,(3,3),0)
gaus_sp_img2 = cv2.GaussianBlur(sp_img2,(3,3),0)

#se le aplica mediana
mediana_gn_img = cv2.medianBlur(gn_img,3)
mediana_sp_img = cv2.medianBlur(sp_img,3)
mediana_gn_img2 = cv2.medianBlur(gn_img2,3)
mediana_sp_img2 = cv2.medianBlur(sp_img2,3)

#se le aplica minimo
min_gn_img = cv2.erode(gn_img, (3,3))
min_sp_img = cv2.erode(sp_img, (3,3))
min_gn_img2 = cv2.erode(gn_img2, (3,3))
min_sp_img2 = cv2.erode(sp_img2, (3,3))

#se le aplica maximo
max_gn_img = cv2.dilate(gn_img, (3,3))
max_sp_img = cv2.dilate(sp_img, (3,3))
max_gn_img2 = cv2.dilate(gn_img2, (3,3))
max_sp_img2 = cv2.dilate(sp_img2, (3,3))

cv2.imshow("imagen",img)
cv2.imshow("gaussiano",gn_img)
cv2.imshow("sal y pimienta",sp_img)
cv2.imshow("media gauss",media_gn_img)
cv2.imshow("media sal y pimienta",media_sp_img)
cv2.imshow("gauss gauss",gaus_gn_img)
cv2.imshow("gauss sal y pimienta",gaus_sp_img)
cv2.imshow("mediana gauss",mediana_gn_img)
cv2.imshow("mediana sal y pimienta",mediana_sp_img)
cv2.imshow("minimo gauss",min_gn_img)
cv2.imshow("minimo sal y pimienta",min_sp_img)
cv2.imshow("maximo gauss",max_gn_img)
cv2.imshow("maximo sal y pimienta",max_sp_img)


cv2.imshow("imagen2",img2)
cv2.imshow("gaussiano2",gn_img2)
cv2.imshow("sal y pimienta2",sp_img2)
cv2.imshow("media gauss2",media_gn_img2)
cv2.imshow("media sal y pimienta2",media_sp_img2)
cv2.imshow("gauss gauss2",gaus_gn_img2)
cv2.imshow("gauss sal y pimienta2",gaus_sp_img2)
cv2.imshow("mediana gauss2",mediana_gn_img2)
cv2.imshow("mediana sal y pimienta2",mediana_sp_img2)
cv2.imshow("minimo gauss2",min_gn_img2)
cv2.imshow("minimo sal y pimienta2",min_sp_img2)
cv2.imshow("maximo gauss2",max_gn_img2)
cv2.imshow("maximo sal y pimienta2",max_sp_img2)


cv2.waitKey(0)
cv2.destroyAllWindows()