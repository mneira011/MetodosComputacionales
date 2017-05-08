import matplotlib.pyplot as plt
import numpy as np

def genGraph(nombre):
    data = np.loadtxt(nombre + ".dat",delimiter = ",")
    plt.figure( figsize=(6, 6))
    plt.imshow(data)
    # plt.colorbar()
    cbar = plt.colorbar()
    cbar.set_label(r'$Temperatura\ (^\circ\ C)$')
    plt.xlabel(r"$x\ (cm)$")
    plt.ylabel(r"$y\ (cm)$")
    plt.savefig(nombre+".png")
    plt.close()


plt.figure( figsize=(8, 8))

data = np.loadtxt("promAbiertasCte.dat")
xs = np.linspace(0,2500,len(data))
plt.plot(xs,data,label='Abiertas')
data = np.loadtxt("promFijasCte.dat")
xs = np.linspace(0,2500,len(data))
plt.plot(xs,data,label = 'Fijas')
data = np.loadtxt("promPeriodicasCte.dat")
xs = np.linspace(0,2500,len(data))
plt.plot(xs,data,label='Periodicas')
plt.legend(loc= 'best')
plt.title(r"$100^\circ\ C\ constante$",fontsize =20)
plt.xlabel(r"$Tiempo\ (s)$")
plt.ylabel(r"$Temperatura\ promedio\ (^\circ C)$")
plt.savefig("promCaso1.png")

plt.close()

plt.figure( figsize=(8, 8))

data = np.loadtxt("promAbiertasNOCte.dat")
xs = np.linspace(0,2500,len(data))
plt.plot(xs,data,label = "Abiertas")
data = np.loadtxt("promFijasNOCte.dat")
xs = np.linspace(0,2500,len(data))
plt.plot(xs,data,label = "Fijas")
data = np.loadtxt("promPeriodicasNOCte.dat")
xs = np.linspace(0,2500,len(data))
plt.plot(xs,data,label = "Periodicas")
plt.legend(loc = 'best')
plt.title(r"$100^\circ\ C\ NO\ constante$",fontsize =20)
plt.xlabel(r"$Tiempo\ (s)$")
plt.ylabel(r"$Temperatura\ promedio\ (^\circ C)$")
plt.savefig("promCaso2.png")

plt.close()



genGraph("fijasNOCte0")
genGraph("fijasNOCte100")
genGraph("fijasNOCte2500")

genGraph("fijasCte0")
genGraph("fijasCte100")
genGraph("fijasCte2500")

genGraph("periodicasNOCte0")
genGraph("periodicasNOCte100")
genGraph("periodicasNOCte2500")

genGraph("periodicasCte0")
genGraph("periodicasCte100")
genGraph("periodicasCte2500")

genGraph("abiertasNOCte0")
genGraph("abiertasNOCte100")
genGraph("abiertasNOCte2500")

genGraph("abiertasCte0")
genGraph("abiertasCte100")
genGraph("abiertasCte2500")
