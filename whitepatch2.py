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
                    wp[i,j,k]=((255*(base[i,j,k]))/maximoazul)
                if(k==1):
                    wp[i,j,k]=((255*(base[i,j,k]))/maximoverde)
                if(k==2):
                    wp[i,j,k]=((255*(base[i,j,k]))/maximorojo)
 
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
                            
def cambiarcolor(nuevo,base,color):
    for i in range(filas):
        for j in range(columnas):
            for k in range(colores):
                nuevo[i,j,k]=base[i,j,k]
                if(k!=color):
                    nuevo[i,j,k]=base[i,j,k]*0.5
                    if(nuevo[i,j,k]>255):
                        nuevo[i,j,k]=255

"""Se define la imagen que se va a usar, su tamaño, su version float64 y su arreglo whitepatch vacio"""
img=cv2.imread("C:\\Users\\Usuario.DESKTOP-L133VTH\\Desktop\\manos.jpg",cv2.IMREAD_COLOR)
img_64=np.asarray(img,dtype=np.float64)
filas=img.shape[0]
columnas=img.shape[1]
colores=3
imgwp=np.zeros([filas,columnas,colores])

"""Se crea la imagen roja y su array whitepatch vacio"""
rojo=np.zeros([filas,columnas,colores])
cambiarcolor(rojo,img,2)
rojo_8=np.asarray(rojo,dtype=np.uint8)
rojowp=np.zeros([filas,columnas,colores])

"""Se crea la imagen azul y su array whitepatch vacio"""
azul=np.zeros([filas,columnas,colores])
cambiarcolor(azul,img,0)
azul_8=np.asarray(azul,dtype=np.uint8)
azulwp=np.zeros([filas,columnas,colores])

"""Se crea la imagen verde y su array whitepatch vacio"""
verde=np.zeros([filas,columnas,colores])
cambiarcolor(verde,img,1)
verde_8=np.asarray(verde,dtype=np.uint8)
verdewp=np.zeros([filas,columnas,colores])

"""Se definen maximos y minimos de la imagen a diferenciar, y el array vacio de las imagenes diferenciadas"""
dfimgwp=np.zeros([filas,columnas])
dfrojowp=np.zeros([filas,columnas])
dfazulwp=np.zeros([filas,columnas])
dfverdewp=np.zeros([filas,columnas])

"""Se definen maximos y minimos de la imagen a diferenciar, y el array vacio de las imagenes diferenciadas (cambio de color)"""
maxi=np.array([205,216,241],np.uint8)
mini=np.array([49,71,153],np.uint8)
dfimg=np.zeros([filas,columnas])
dfazul=np.zeros([filas,columnas])
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

diferenciar(maxi,mini,dfimg,img)
diferenciar(maxi,mini,dfazul,azul_8)
diferenciar(maxi,mini,dfrojo,rojo_8)
diferenciar(maxi,mini,dfverde,verde_8)

diferenciar(maxi,mini,dfimgwp,imgwp_8)
diferenciar(maxi,mini,dfazulwp,azulwp_8)
diferenciar(maxi,mini,dfrojowp,rojowp_8)
diferenciar(maxi,mini,dfverdewp,verdewp_8)

cv2.imshow("imagen",img)
cv2.imshow("roja",rojo_8)
cv2.imshow("azul",azul_8)
cv2.imshow("verde",verde_8)

cv2.imshow("whitepatch rojo",rojowp_8)
cv2.imshow("whitepatch azul",azulwp_8)
cv2.imshow("whitepatch verde",verdewp_8)
cv2.imshow("whitepatch original",imgwp_8)

cv2.imshow("diferenciada rojo",dfrojo)
cv2.imshow("diferenciada azul",dfazul)
cv2.imshow("diferenciada verde",dfverde)
cv2.imshow("diferenciada imagen",dfimg)

cv2.imshow("diferenciada rojo whitepatch",dfrojowp)
cv2.imshow("diferenciada azul whitepatch",dfazulwp)
cv2.imshow("diferenciada verde whitepatch",dfverdewp)
cv2.imshow("diferenciada imagen whitepatch",dfimgwp)



cv2.waitKey(0)
cv2.destroyAllWindows()