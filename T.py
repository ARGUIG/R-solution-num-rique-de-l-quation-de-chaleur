from math import *
import numpy as np
import matplotlib.pyplot as plt

L=1       #Longueur de la barre
tau=1     #Duree totale evolution
nx=100    #Nombre de tronçons
nt=10000  #Nombre intervalles de temps
Dx=L/nx   #Longueur tronçon
Dt=tau/nt #Intervalle elementaire de temps
D=0.5     #Coefficient de difusion thermique
T0=100    #Temperature initiale de la barre
Tex=0     #Temperature des extremites

x=np.linspace(0,L,nx)
T=100*[T0]
T[0],T[-1]=Tex,Tex
accroissT=np.zeros(nx)

for n in range(nt):
    for m in range(1,nx-1):
        a=(Dt*D)/(Dx**2)
        accroissT[m]=a*(T[m+1]+T[m-1]-2*T[m])
    for m in range(1,nx-1):
        T[m]+=accroissT[m]
    if (n%1000==0):
        plotlabel= 't=%1.2f s'%(n*Dt)
        plt.plot(x,T,label=plotlabel)

plt.title('Evolution de la temperature')
plt.axis([0,L,0,105])
plt.legend()
plt.xlabel('x(m)',fontsize=18)
plt.ylabel('T(K)',fontsize=18)
plt.grid()
plt.show()
