# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 13:09:41 2023

@author: super
"""

def cuatro_reinas(fila):
    k=0  # inicia en la columna 0, que es la primera
    n=len(fila)
    # como fila(k) se incrementa antes de usarla, se hace fila(0) igual a -1, que es la posicion inexistente 0
    fila[k]=-1

    while k>-1:
        fila[k]+=1
        # se busca un movimiento legal en la columna k
        while(fila[k]<n) and conflicto(fila,k):
            fila[k]+= 1
        if fila[k]<n:
            if k==n-1:
                return True
            else:
                k+=1  # siguiente columna
                fila[k]=-1
        else:
            k-=1  # regresar a columna anterior
    return False  # no hay solución


def conflicto(fila,columna):
    for i in range(columna):
        if fila[i]==fila[columna] or fila[i]-fila[columna]==columna-i or fila[columna]-fila[i]==columna-i:
            return True
    return False


fila = [-1,-1,-1,-1]
if cuatro_reinas(fila) == True:
    print(fila)
else:
    print("No es posible")