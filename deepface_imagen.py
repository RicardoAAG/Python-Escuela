# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 20:48:23 2023

@author: Usuario
"""

from deepface import DeepFace
import cv2

uno=cv2.imread("C:\\Users\\Usuario\\Desktop\\bd\\danny.jpg",cv2.IMREAD_COLOR)
dos=cv2.imread("C:\\Users\\Usuario\\Desktop\\img1.jpg",cv2.IMREAD_COLOR)

result = DeepFace.verify(img1_path = "C:\\Users\\Usuario\\Desktop\\bd\\danny.jpg", img2_path = "C:\\Users\\Usuario\\Desktop\\img1.jpg")

x=result.get("facial_areas").get("img1").get("x")
y=result.get("facial_areas").get("img1").get("y")
w=result.get("facial_areas").get("img1").get("w")
h=result.get("facial_areas").get("img1").get("h")

x2=result.get("facial_areas").get("img2").get("x")
y2=result.get("facial_areas").get("img2").get("y")
w2=result.get("facial_areas").get("img2").get("w")
h2=result.get("facial_areas").get("img2").get("h")

cv2.rectangle(uno, (x, y), (x + w, y + h), (255), 2)
cv2.rectangle(dos, (x2, y2), (x2 + w2, y2 + h2), (255), 2)

cv2.imshow("uno",uno)
cv2.imshow("dos",dos)

cv2.waitKey(0)
cv2.destroyAllWindows()