import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
	return a * np.sin(b*x+c)+d

datos = np.loadtxt("solar.dat")

print np.shape(datos)

n_manchas_total = datos[:,3]
tiempo_total = datos[:,0]+(datos[:,1]-1.0)/12.0

n_manchas = n_manchas_total[n_manchas_total>0]
tiempo = tiempo_total[n_manchas_total>0] 

popt, pcov = curve_fit(func, tiempo, n_manchas)

print popt


import matplotlib.pyplot as plt 

fig = plt.figure()
ax = plt.axes()


ax.set_xlabel("Time [years]")
ax.set_ylabel("Spot number")
ax.set_title("comparision")


plt.scatter(tiempo, n_manchas, label="observations", s=0.2)


x = np.linspace(np.amin(tiempo), np.amax(tiempo), 200)
y = func(x, popt[0], popt[1], popt[2], popt[3])
plt.plot(x,y, label="Fit!")

ax.legend()

plt.savefig('resultado.pdf')
plt.close()




