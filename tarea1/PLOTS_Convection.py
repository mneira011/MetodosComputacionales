import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate 

datos = open("TempHeight.txt")
for i in range(7):
    datos.readline()
c = datos.readlines()
datos =np.loadtxt(c)

alt = datos[:,0]
temp = datos[:,1]

plt.figure(figsize=(10,10))
plt.scatter(alt,temp,c="r")
plt.xlabel(r"$Altura\ (m)$",fontsize = 15)
plt.ylabel(r"$Temperatura\ (^\circ C)$",fontsize = 15)
plt.title(r"$Temperatura\ vs\ Altura$",fontsize = 30)

plt.savefig("TemperaturePlot.pdf")

xs = np.linspace(2500,25000,150)

tck  = interpolate.splrep(alt, temp,k=5)
y_spline = interpolate.splev(xs,tck)

def diff_central(ys,xs):
	h = xs[1]-xs[0]
	f = ys
	f_prime_diff = (f[2:-1] - f[0:-3])/(2*h)
	return (xs[1:-2],f_prime_diff)
xs,ys = diff_central(y_spline,xs)
def linea(x):
    return -9800

plt.figure(figsize=(10,10))
plt.plot(xs,ys,label ="Gradiente vertical")
ys1 = []
for i in xs:
    ys1.append(-0.0098)
ys1 = np.array(ys1)
plt.plot(xs,ys1,label ="Gradiente adiabatico")
plt.xlabel(r"$Altura\ (m)$",fontsize = 15)
plt.ylabel(r"$dT/dz\ (^\circ C/m)$",fontsize = 15)
plt.title(r"$Grad.\ vertical\ vs\ Altura$",fontsize = 30)
plt.legend(loc = 3)
plt.savefig("GradientsPlot.pdf")


yind= np.where(abs(ys)>=0.0098)
plt.figure(figsize=(10,10))
plt.scatter(xs[yind[0]],ys[yind[0]])
plt.xlabel(r"$Altura\ (m)$",fontsize = 15)
plt.ylabel(r"$dT/dz\ (^\circ C/m)$",fontsize = 15)
plt.title(r"$Grad.\ vertical\ vs\ Altura$",fontsize = 30)

plt.savefig("ConvectionPLOT.pdf")
