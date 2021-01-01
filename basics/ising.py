# -*- coding: utf-8 -*-
"""
@author: Manuel Alejandro Segura D
"""

from random import randint, uniform
import numpy as np
import math
import matplotlib.pyplot as plt
#Creacion de la matriz spin y parametro beta
beta=1
n=20
m=20
matrix=np.zeros((n,m))
spin=[-1,1]
for i in range(n):
    for j in range(m):
        matrix[i,j]=spin[randint(0,1)]    
matrixi=matrix    
def energia(matriz):
#Parametro J
    J=-1
    n=matriz.shape[0]
    m=matriz.shape[1]
#    ens=np.zeros((n,m))
    iz=0
    dr=0
    ar=0
    ab=0
    energia=0
    for i in range(n):
        for j in range(m):
            iz=j-1
            dr=j+1
            ar=i-1
            ab=i+1
            if iz is -1:
               iz=m-1
            if dr is m:
               dr=0
            if ar is -1:
               ar=m-1
            if ab is m:
               ab=0
#            ens[i,j]=matriz[i,j]*(matriz[ar,j]+matriz[ab,j]+matriz[i,iz]+matriz[i,dr])   
            energia=energia+matriz[i,j]*(matriz[ar,j]+matriz[ab,j]+matriz[i,iz]+matriz[i,dr])
#    print(ens)        
    return -J*energia/2

def paso(matriz, d):
    #Parametro beta
    beta=1/d
    n=matriz.shape[0]
    m=matriz.shape[1]
    x=randint(0,m-1)
    y=randint(0,n-1)
    matriz1=matriz
    energia1=energia(matriz1)
    matriz[y,x]=matriz[y,x]*-1
    energia2=energia(matriz)
    deltaen=energia2-energia1
    p=uniform(0,1)
    #Funcion peso e^(-b*dE)
    peso=math.exp(-beta*deltaen)
    if deltaen>0 and peso<p:
       rpta=matriz1
    else:
        rpta=matriz
    return rpta
energias=[]
energias.append(energia(matrix))
for i in range(1000):
    matrix=paso(matrix, 2.26)
    energias.append(energia(matrix))
magnetizaciones=[]
magnetizacion=np.sum(matrix.ravel())
magnetizaciones.append(magnetizacion)
print('Energia promedio', np.average(energias))
print('Magnetizacion promedio', np.average(magnetizaciones))
fig=plt.figure(1)
plt.plot(energias)
plt.title('Energia')
plt.xlabel('Iteraciones')
plt.ylabel('energia')
fig.savefig('energias.png')
pmags=[]
pens=[]
temps=[]
#Varias temperaturas
for k in range(100):
    energias=[]
    energias.append(energia(matrix))
    for i in range(1000):
        matrix=paso(matrix, 0.5+k/100)
        energias.append(energia(matrix))
    magnetizaciones=[]
    magnetizacion=np.sum(matrix.ravel())
    magnetizaciones.append(magnetizacion)
    pmags.append(np.average(magnetizaciones))
    pens.append(np.average(energias))
    temps.append(0.5+k/100)
fig=plt.figure(2)
plt.plot(temps,pens)
plt.title('Energia promedio')
plt.xlabel('temperaturas')
plt.ylabel('energia')
fig.savefig('energiast.png')
fig=plt.figure(3)
plt.plot(temps,pmags)
plt.title('Magnetizacion promedio')
plt.xlabel('temperatura')
plt.ylabel('magnetizacion')
fig.savefig('magst.png')
