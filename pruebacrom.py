# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:33:44 2023

@author: super

bn=cv2.inRange(img,mini,maxi)

"""

import cv2
import numpy as np

"""Funcion para cromatizar"""
def cromatico(cromatica,base):
    for i in range(filas):
        for j in range(columnas):      
            for k in range(colores):
                cromatica[i,j,k]=((base[i,j,k])/(base[i,j,0]+base[i,j,1]+base[i,j,2]))
 
"""Funcion para diferenciar 64"""
def diferenciar64(maximo,minimo,diferenciada,base):
    base=base[:,:,:]*(255)
    for i in range(filas):
        for j in range(columnas):      
                if(minimo[0]<=base[i,j,0]<=maximo[0]):
                    if(minimo[1]<=base[i,j,1]<=maximo[1]):
                        if(minimo[2]<=base[i,j,2]<=maximo[2]):
                            diferenciada[i,j]=255
                            
"""Funcion para diferenciar"""
def diferenciar(maximo,minimo,diferenciada,base):
    for i in range(filas):
        for j in range(columnas):      
                if(minimo[0]<=base[i,j,0]<=maximo[0]):
                    if(minimo[1]<=base[i,j,1]<=maximo[1]):
                        if(minimo[2]<=base[i,j,2]<=maximo[2]):
                            diferenciada[i,j]=255

"""Se define la imagen que se va a usar, su tamaño, su version float64 y su arreglo cromatico vacio"""
img=cv2.imread("C:\\Users\\Usuario.DESKTOP-L133VTH\\Desktop\\manos.jpg",cv2.IMREAD_COLOR)
img_64=np.asarray(img,dtype=np.float64)
filas=img.shape[0]
columnas=img.shape[1]
colores=3
imgcrom=np.zeros([filas,columnas,colores])

"""Se crea la imagen oscura y su array cromatico vacio"""
osc=img[:,:,:]*(0.6)
osc_8=np.asarray(osc,dtype=np.uint8)
osccrom=np.zeros([filas,columnas,colores])

"""Se crea la SEGUNDA imagen oscura y su array cromatico vacio"""
osc2=img[:,:,:]*(0.2)
osc2_8=np.asarray(osc2,dtype=np.uint8)
osccrom2=np.zeros([filas,columnas,colores])

"""Se definen maximos y minimos de la imagen a diferenciar, y el array vacio de las imagenes diferenciadas"""
maxi=np.array([80,84,155],np.uint8)
mini=np.array([25,50,90],np.uint8)
dfimg=np.zeros([filas,columnas])
dfcrom=np.zeros([filas,columnas])
dfcrom2=np.zeros([filas,columnas])

"""Se definen maximos y minimos de la imagen a diferenciar, y el array vacio de las imagenes diferenciadas (oscuras)"""
maxi2=np.array([205,216,241],np.uint8)
mini2=np.array([49,71,153],np.uint8)
dfimgosc=np.zeros([filas,columnas])
dfcromosc=np.zeros([filas,columnas])
dfcromosc2=np.zeros([filas,columnas])

cromatico(imgcrom,img_64)
cromatico(osccrom,osc)
cromatico(osccrom2,osc2)
diferenciar64(maxi,mini,dfcrom,osccrom)
diferenciar64(maxi,mini,dfcrom2,osccrom2)
diferenciar64(maxi,mini,dfimg,imgcrom)

diferenciar(maxi2,mini2,dfimgosc,img)
diferenciar(maxi2,mini2,dfcromosc,osc_8)
diferenciar(maxi2,mini2,dfcromosc2,osc2_8)

cv2.imshow("imagen",img)
cv2.imshow("cromatico original",imgcrom)
cv2.imshow("oscuro",osc_8)
cv2.imshow("cromatico",osccrom)
cv2.imshow("oscuro2",osc2_8)
cv2.imshow("cromatico2",osccrom2)
cv2.imshow("diferenciada original",dfimg)
cv2.imshow("diferenciada cromatica",dfcrom)
cv2.imshow("diferenciada cromatica2",dfcrom2)

cv2.imshow("diferenciada original sin crom",dfimgosc)
cv2.imshow("diferenciada oscura sin crom",dfcromosc)
cv2.imshow("diferenciada oscura2 sin crom",dfcromosc2)


cv2.waitKey(0)
cv2.destroyAllWindows()