import math
import numpy as np
import matplotlib.pyplot as plt


a = 1
b = 1
angulo = np.linspace(0, 6*np.pi, 100)
x = []
y = []

for i in angulo:
    x.append( (a + b*i)*np.cos(i) )
    y.append( (a + b*i)*np.sin(i) )

plt.figure()
plt.plot(x,y, color='black')

plt.savefig("espiral.png")
