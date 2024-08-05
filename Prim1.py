# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:36:40 2023

@author: super
"""

def prim(a,n,s):
    agregados=[]
    suma=0
    while(len(agregados)!=n):
        agregados.append(0)
    agregados[s]=1
    final=[]
    for i in range(0,n-2):
        min=m
        for j in range(0,n):
            if(agregados[j]==1):
                for k in range(0,n):
                    if(agregados[k]==0 and a[j][k]<min):
                        agregar_vertice=k
                        e=[j,k]
                        min=a[j][k]
        agregados[agregar_vertice]=1
        final.append(e)
        suma+=a[e[0]][e[1]]
        print(a[e[0]][e[1]])
    return [final,suma]


m=999
n=7

INICIO=1

#Vertice 0 no existe, pero es necesario para que inicie desde 1
w=[#0 1 2 3 4 5 6
   [m,m,m,m,m,m,m],#0
   [m,m,4,2,m,3,m],#1
   [m,4,m,m,5,m,m],#2
   [m,2,m,m,1,6,3],#3
   [m,m,5,1,m,m,6],#4
   [m,3,m,6,m,m,2],#5
   [m,m,m,3,6,2,m],#6
]


print(prim(w,n,INICIO))