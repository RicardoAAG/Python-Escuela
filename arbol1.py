# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:48:01 2023

@author: Usuario
"""

Vaux=[]
E=[('a','b'),('b','g'),('b','d'),('d','f'),('f','h'),('e','f'),('c','d'),('c','e'),('a','g'),('a','g'),('e','g')]
V=['a','b','c','d','e','f','g','h']

def bla(F,V):
    S=[]
    S.append(V[0])
    V1=[]
    V1.append(V[0])    
    E1=[]
    S1=[]
    while True:
        boo = True
        for x in S:
            diferenciar(V,V1)
            for y in Vaux:
                z=(x,y)
                if z in E:
                    E1.append(z)
                    V1.append(y)
                    S1.append(y)
                    boo = False
        if boo:
            print(V1)
            print(E1)
            return V1+E1
        S=S1
        S1=[]
        
def diferenciar(A,B):
    for i in B:
        for i in A:
            if i in Vaux:
                Vaux.remove(i)

bla(E,V)