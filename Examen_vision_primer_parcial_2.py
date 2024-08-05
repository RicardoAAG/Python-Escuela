# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 21:37:00 2023

@author: super
"""

import cv2
import numpy as np


img=cv2.imread("C:\\Users\\super\\OneDrive\\Escritorio\\cubo.jpg",0)

""""Kernels"""
""""Sobel"""
k_sobelx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
k_sobely=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

""""Prewitt"""
k_prewittx=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
k_prewitty=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

""""Roberts"""
k_robertsx=np.array([[1,0],[0,-1]])
k_robertsy=np.array([[0,1],[-1,0]])

"""Filtros"""
""""Sobel"""
sobelx=cv2.filter2D(img,-1,k_sobelx)
sobely=cv2.filter2D(img,-1,k_sobely)
sobel=sobelx+sobely

""""Prewitt"""
prewittx=cv2.filter2D(img,-1,k_prewittx)
prewitty=cv2.filter2D(img,-1,k_prewitty)
prewitt=prewittx+prewitty

""""Roberts"""
robertsx=cv2.filter2D(img,-1,k_robertsx)
robertsy=cv2.filter2D(img,-1,k_robertsy)
roberts=robertsx+robertsy


cv2.imshow('Imagen', img)
cv2.imshow('Sobel', sobel)
cv2.imshow('Prewitt', prewitt)
cv2.imshow('Roberts', roberts)


cv2.waitKey(0)
cv2.destroyAllWindows()