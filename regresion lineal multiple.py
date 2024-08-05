# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:27:13 2023

@author: super
"""
#Librerias
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split

#Importamos el dataset de scikit-learn
boston = datasets.load_boston()
print(boston)
print()

#verificar la informacion que hay en el dataset
print("Informacion en el dataset: ")
print(boston.keys())
print()
#data, todas las variables que determinan el precio de las casas divididas en columnas
#target, la columna con los precios finales
#feature_names, nombre de cada columna del data
#DESCR, descripcion de cada columna

#verifica las caracteristicas de cada columna
print("Caracteristicas por columna del dataset: ")
print(boston.DESCR)
#se tienen 13 variables a tomar en cuenta para el valor de la casa
#se tienen 506 casas de muestra, junto con su precio

#verificar que la cantidad de datos es correcta
print("Cantidad de casas: ")
print(boston.data.shape[0])
print()
print("Cantidad de variables: ")
print(boston.data.shape[1])
print()

#verificar las etiquetas de cada variable/columna
print("Nombres de variables/columnas a tomar en cuenta: ")
print(boston.feature_names)
print()


#solo vamos a tomar RM (numero de habitaciones), AGE (proportion of owner-occupied units built prior to 1940), DIS (ditancia a centros de trabajos de Boston)
#que se encuentran en las columnas 5, 6 y 7, y esas se asignan a una variable llamada X mutiple
X_multiple = boston.data[:,5:8]
print(X_multiple)
print()

#definimos Y como el valor de las casas ya conoocidos
y_multiple=boston.target


#separamos los datos en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test=train_test_split(X_multiple,y_multiple,test_size=0.2)

#definimos el alogoritmo a utilizar, se va a usar el de regresion lineal
lr_multiple = linear_model.LinearRegression()

#entrenamos el modelo con las variables de entrenamiento, que equivalen a 2/3 del total de datos
lr_multiple.fit(X_train,y_train)

#revisamos que tan bien funciona el modelo usando los datos de prueba
Y_pred_multiple=lr_multiple.predict(X_test)


#finalmente obtenemos los valores de la ecuacion
print("DATOS DEL MODELO GENERADO:")
print()
print("Valores de las pendientes: ")
print(lr_multiple.coef_)
print()
print("Valores de la interseccion o coeficiente: ")
print(lr_multiple.intercept_)
print()
print("Valores de la interseccion o coeficiente: ")
print(lr_multiple.score(X_train,y_train))
print()