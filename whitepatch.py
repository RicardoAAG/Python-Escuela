# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:11:43 2023

@author: super
"""

import cv2
import numpy as np

"""Funcion para aplicar whitepatch"""
def whitepatch(wp,base):
    maximorojo=base[:,:,2].max()
    maximoazul=base[:,:,0].max()
    maximoverde=base[:,:,1].max()
    print(maximorojo)
    print(maximoazul)
    print(maximoverde)
    for i in range(filas):
        for j in range(columnas):      
            for k in range(colores):
                if(k==0):
                    wp[i,j,k]=((255*(base[i,j,0]))/maximoazul)
                if(k==1):
                    wp[i,j,k]=((255*(base[i,j,1]))/maximoverde)
                if(k==2):
                    wp[i,j,k]=((255*(base[i,j,2]))/maximorojo)
 

"""Funcion para diferenciar"""
def diferenciar(maximo,minimo,diferenciada,base):
    for i in range(filas):
        for j in range(columnas):      
                if(minimo[0]<=base[i,j,0]<=maximo[0]):
                    if(minimo[1]<=base[i,j,1]<=maximo[1]):
                        if(minimo[2]<=base[i,j,2]<=maximo[2]):
                            diferenciada[i,j]=255
                            
def cambiarcolor(nuevo,base,color):
    for i in range(filas):
        for j in range(columnas):
            for k in range(colores):
                """nuevo[i,j,k]=base[i,j,k]"""
                if(k==color):
                    nuevo[i,j,k]=nuevo[i,j,k]+50
                    if(nuevo[i,j,k]>255):
                        nuevo[i,j,k]=255

"""Se define la imagen que se va a usar, su tamaño, su version float64 y su arreglo whitepatch vacio"""
img=cv2.imread("C:\\Users\\Usuario\\Desktop\\INE.png",cv2.IMREAD_COLOR)
img_64=np.asarray(img,dtype=np.float64)
filas=img.shape[0]
columnas=img.shape[1]
colores=3
imgwp=np.zeros([filas,columnas,colores])

"""Se crea la imagen roja y su array whitepatch vacio"""
rojo=np.copy(img)
rojo=np.asarray(rojo,dtype=np.float64)
cambiarcolor(rojo,img,2)
rojo_8=np.asarray(rojo,dtype=np.uint8)
rojowp=np.zeros([filas,columnas,colores])

"""Se crea la imagen azul y su array whitepatch vacio"""
azul=np.copy(img)
azul=np.asarray(azul,dtype=np.float64)
cambiarcolor(azul,img,0)
azul_8=np.asarray(azul,dtype=np.uint8)
azulwp=np.zeros([filas,columnas,colores])

"""Se crea la imagen verde y su array whitepatch vacio"""
verde=np.copy(img)
verde=np.asarray(verde,dtype=np.float64)
cambiarcolor(verde,img,1)
verde_8=np.asarray(verde,dtype=np.uint8)
verdewp=np.zeros([filas,columnas,colores])

"""Se definen maximos y minimos de la imagen a diferenciar, y el array vacio de las imagenes diferenciadas"""
maxi=np.array([80,84,155],np.uint8)
mini=np.array([25,50,90],np.uint8)
dfimgwp=np.zeros([filas,columnas])
dfrojowp=np.zeros([filas,columnas])
dfazulwp=np.zeros([filas,columnas])
dfverdewp=np.zeros([filas,columnas])

"""Se definen maximos y minimos de la imagen a diferenciar, y el array vacio de las imagenes diferenciadas (cambio de color)"""
maxi2=np.array([205,216,241],np.uint8)
mini2=np.array([49,71,153],np.uint8)
dfimg=np.zeros([filas,columnas])
dfauzl=np.zeros([filas,columnas])
dfrojo=np.zeros([filas,columnas])
dfverde=np.zeros([filas,columnas])

whitepatch(rojowp,rojo)
rojowp_8=np.asarray(rojowp,dtype=np.uint8)
whitepatch(azulwp,azul)
azulwp_8=np.asarray(azulwp,dtype=np.uint8)
whitepatch(verdewp,verde)
verdewp_8=np.asarray(verdewp,dtype=np.uint8)
whitepatch(imgwp,img)
imgwp_8=np.asarray(imgwp,dtype=np.uint8)
"""cromatico(osccrom,osc)
cromatico(osccrom2,osc2)
diferenciar64(maxi,mini,dfcrom,osccrom)
diferenciar64(maxi,mini,dfcrom2,osccrom2)
diferenciar64(maxi,mini,dfimg,imgcrom)

diferenciar(maxi2,mini2,dfimgosc,img)
diferenciar(maxi2,mini2,dfcromosc,osc_8)
diferenciar(maxi2,mini2,dfcromosc2,osc2_8)"""

cv2.imshow("imagen",img)
cv2.imshow("roja",rojo_8)
cv2.imshow("azul",azul_8)
cv2.imshow("verde",verde_8)
cv2.imshow("whitepatch rojo",rojowp_8)
cv2.imshow("whitepatch azul",azulwp_8)
cv2.imshow("whitepatch verde",verdewp_8)
cv2.imshow("whitepatch original",imgwp_8)
"""cv2.imshow("cromatico",osccrom)
cv2.imshow("cromatico2",osccrom2)
cv2.imshow("diferenciada original",dfimg)
cv2.imshow("diferenciada cromatica",dfcrom)
cv2.imshow("diferenciada cromatica2",dfcrom2)

cv2.imshow("diferenciada original sin crom",dfimgosc)
cv2.imshow("diferenciada oscura sin crom",dfcromosc)
cv2.imshow("diferenciada oscura2 sin crom",dfcromosc2)"""


cv2.waitKey(0)
cv2.destroyAllWindows()