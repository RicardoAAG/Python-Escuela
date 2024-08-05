# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:12:00 2023

@author: super
"""

import numpy as np   
    
    
vertices={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
aristas={"A":"B","A":"C","A":"G","A":"G","C":"E","G":"E","E":"F","F":"D","D":"C","B":"D","B":"G","F":"H"}
inicio={1:vertices[1]}

S=inicio
Vp=inicio
Ep={}
verdadero=0
adios=0
while(adios==0):
    for x in S.values():
        verdadero=0
        for k in S.keys():
            del vertices[k]
            Vn=vertices
        for y in Vn.values():
            if x in aristas:
                if aristas[x]==y:
                    Ep[x]=y
                    verdadero=1
    if verdadero==0:
        print("adios")
        adios=1