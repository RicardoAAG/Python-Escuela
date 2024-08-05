# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 19:53:30 2023

@author: Usuario
"""

import cv2
import numpy as np

X=np.array([-3,-2,-1,0,1,2,3])
Y=np.array([-6,-4,-2,0,2,4,6])
W=4
sumatoria=0

for i in range(7):
    Yg=W*X[i]
    sumatoria=sumatoria+(Yg-Y[i])*(Yg-Y[i])
    print(sumatoria)
    
final=(1/(2*(7)))*(sumatoria)
print(final)