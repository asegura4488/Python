import numpy as np
import matplotlib.pyplot as plt
#from tqdm import tqdm 


G= 6.67 * 10**(-17) #N km^2 kg^-2

M_Earth=5.9736 * 10**(24) #masa de la Tierra en kg

R_Earth=6.3781 * 10**3 #Radio terrestre en km

M_moon=0.07349 * 10**24

R_moon=1.7374 * 10**3

d=3.844 * 10**5 

omega=2.6617*3600* 10**(-6) #Vel angular de la Orbita lunar 

m= 15000.0 #masa de la nave en kg

def ODE(t,q0):

	r = q0[0]
	theta = q0[1]
	u = q0[2] 
	w = q0[3]
	f = np.zeros(4)
	f[0] = u
	f[1] = w/r**2 
	f[2] = -(w**2/r)+((G*m*M_Earth)/r**2)+((G*m*M_moon)/(np.sqrt(r**2+d**2-2*r*d*np.cos(theta-omega*t)))**3)*(r-d*np.cos(theta-omega*t))
	f[3] = ((G*m*M_moon)/(np.sqrt(r**2+d**2-2*r*d*np.cos(theta-omega*t)))**3)*(r*d*np.sin(theta-omega*t))
	return f

'''
def f1(t,r,theta,u,w):
	return u
def f2(t,r,theta,u,w):
	return w/r**2
def f3(t,r,theta,u,w):
	return -(w**2/r)+((G*m*M_Earth)/r**2)+((G*m*M_moon)/(np.sqrt(r**2+d**2-2*r*d*np.cos(theta-omega*t)))**3)*(r-d*np.cos(theta-omega*t))
def f4(t,r,theta,u,w):
	return ((G*m*M_moon)/(np.sqrt(r**2+d**2-2*r*d*np.cos(theta-omega*t)))**3)*(r*d*np.sin(theta-omega*t))
'''

#paso del método

n=100000
t0=0.0
tf=100
h=(tf-t0)/n
print("Paso en RK4")
print("h=",h)

# Condiciones iniciales

def RK4(ODE, h, t0, q0):

	k11 = h*ODE(t0, q0)
	
	k21 = h*ODE(t0 + h/2, q0 + k11/2)

	k31 = h*ODE(t0 + h/2, q0 + k21/2)

	k41 = h*ODE(t0 + h, q0 + k31)

	q1 = q0 + (k11 + 2*k21 + 2*k31 + k41)/6

	return q1

# inicializar vectores 
t = np.linspace(t0, tf, n) 
QR = np.zeros([4,n]) 


r0 = R_Earth #km 
v0 = 11.2*3600 #km/h

# Condiciones iniciales
QR[0,0] = R_Earth
QR[1,0] = 0.5
QR[2,0] = v0*np.cos(0.5)
QR[3,0] = 0.01 

for i in range(1,n):
    q0 = QR[:,i-1]
    qf = RK4(ODE, h, 0, q0)
    #cond=cond(qf,h,t,q0)
    QR[:,i] = qf[:]


plt.figure(figsize=(7,4))
plt.plot(t, QR[0,:], color='k', label="r vs t ")
plt.xlabel(r'$t(h)$')
plt.grid()
plt.legend()

plt.figure(figsize=(7,4))
plt.plot(t, QR[1,:], color='k', label="theta vs t ")
plt.xlabel(r'$t(h)$')
plt.grid()
plt.legend()

plt.figure(figsize=(7,4))
plt.plot(t, QR[2,:], color='k', label="v vs t ")
plt.xlabel(r'$t(h)$')
plt.grid()
plt.legend()

plt.figure(figsize=(7,4))
plt.plot(t, QR[3,:], color='k', label="w vs t ")
plt.xlabel(r'$t(h)$')
plt.grid()
plt.legend()

plt.figure(figsize=(7,4))
plt.plot(QR[0,:], QR[2,:], color='k', label="v vs r ")
plt.xlabel(r'$r(km)$')
plt.grid()
plt.legend()



fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(QR[1,:], QR[0,:])
ax.set_rmax(max(QR[0,:]))
ax.grid(True)
plt.show()
