# -*- coding: utf-8 -*-
"""
Created on Sat May  6 23:22:11 2023

@author: super
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:06:45 2023

@author: super
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten

#se carga la base de datos
X_train=np.load.txt('input.csv', delimiter=',')
Y_train=np.load.txt('labels.csv', delimiter=',')

X_test=np.load.txt('input_test.csv', delimiter=',')
Y_test=np.load.txt('labels_test.csv', delimiter=',')

#se reacomoda la base de datos para que quede de la forma 
#(cantidad de imagenes, pixeles de longitud, pixeles de altura, cantidad de canales)
X_train=X_train.reshape(len(X_train),100,100,3)
Y_train=Y_train.reshape(len(Y_train),1)
X_test=X_test.reshape(len(X_test),100,100,3)
Y_test=Y_test.reshape(len(Y_test),1)

#dividimos entre 255 para trabajar con valores de 0 a 1
X_train=X_train/255
X_test=X_test/255

#imprimimos la forma de los array y una imagen de muestra
print("Forma de X_train: ", X_train.shape)
print("Forma de Y_train: ", Y_train.shape)
print("Forma de X_test: ", X_test.shape)
print("Forma de Y_test: ", Y_test.shape)
idx=random.randint(0,len(X_train))
plt.imshow(X_train[idx,:])
plt.show()

#MODELO
#las capas del modelo van a ir en secuencia
model=Sequential([
    #primero las cuatro capas que son una combinacion de 2 filtros convolucionales y 2maxpolin
    Conv2D(32,(3,3),activation='relu',input_shape=(100,100,3)),
    MaxPooling2D((2,2)),
    Conv2D(32,(3,3),activation='relu'),
    MaxPooling2D((2,2)),
    
    #los valores resultantes se juntan en un array de una sola dimension, 
    #y despues se les aplica una red neuronal completamente conectada de 64 neuronas, y la salida final
    Flatten(),
    Dense(64,activation='relu'),
    Dense(10,activation='sigmoid')
])


#ahora vamos a aplicar la funcion de costo y la propagacion lineal para entrenal el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


#ahora vamos a entrenar el modelo
model.fit(X_train,Y_train,epochs=5,batch_size=64)


#ahora evaluamos el modelo en el test dataset
model.evaluate(X_test,Y_test)

#PREDICCION
idx2=random.randint(0,len(Y_test))
plt.imshow(X_test[idx2,:])
plt.show()

y_pred=model.predict(X_test[idx2,:].reshape(1,100,100,3))

y_pred=y_pred>0.5
if(y_pred==0)
	pred='perro'
else
	pred='gato'

print("El numero predicho es: ",pred)