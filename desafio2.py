## DESAFIO 2. Datos de Billboard

## Paso 1. Explorar los datos
# Cargá el dataset usando Pandas y comenzá a explorar los datos.
#Guardá en este espacio todos los procesos y análisis exploratorios que hayas hecho, tanto los preliminares como los definitivos.
#Por favor, indicá cuál(es) es(son) cada uno(s).

import pandas as pd #Importar librería Pandas
import numpy as np #Importar librería Numpy
import matplotlib.pyplot as plt #Importar librería Pyplot de MatPlotLib
import seaborn as sns #Importar librería Seaborn
%matplotlib inline #Para no tener que usar plt.show para ver los gráficos

#renombra las columnas de las semanas:
lista_semanas = [] #se hace esta lista donde se van a ir poniendo los nombres nuevos de cada columna
for col in dfmusic.columns:
    if ".week" in col: #se fija si estamos mirando una columna de 'semana'. Si es así...
        if len(dfmusic[col].name) < 10: #toma las columnas de semanas donde el número de semana tiene un solo dígito
            lista_semanas.append(dfmusic[col].name[1]) #y a esa semana le da el nombre de su número de semana
        else: #a las semanas con número con dos dígitos les da también su número
            lista_semanas.append(dfmusic[col].name[1:3])
    else: #para las columnas que no son semanas, les deja el mismo nombre
        lista_semanas.append(dfmusic[col].name)
dfmusic.columns = lista_semanas #las columnas ahora toman el nombre asignado en la lista lista_semanas previamente
dfmusic.dropna(axis=1, how='all', inplace = True) #remueve todas las columnas donde los valores de toda la fila son NaN.
dfmusic.fillna(value="-",axis=1,inplace = True) #reemplaza todos los valores NaN por "-". A REVISAR.
dfmusic
