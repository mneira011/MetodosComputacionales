import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft

datTrump = wav.read("trumpet.wav")
datViolin = wav.read("violin.wav")
ytrump = (fft(datTrump[1]))/len(datTrump[1])
yviolin =(fft(datViolin[1]))/len(datViolin[1])


xviolin = fftfreq(len(datViolin[1]), 1.0/datViolin[0])
xtrump= fftfreq(len(datTrump[1]), 1.0/datTrump[0])


fig, (ax1,ax2) = plt.subplots(2)
ax1.plot(xtrump,abs(ytrump),label="Trompeta",c = "R")
ax2.plot(xviolin,abs(yviolin),label="Violin")
ax1.set_title("Transf. de fourier",fontsize = 20)
ax2.set_xlabel(r"Frecuencia $(Hz)$")
ax1.set_ylabel("Amplitud")
ax2.set_ylabel("Amplitud")
ax2.set_xlim(-10000,10000)
ax1.set_xlim(-10000,10000)
ax1.legend()
ax2.legend()

plt.savefig("ViolinTrompeta.pdf")
plt.close()

def elimFundamental(frecuencias,intensidades):
    fundamentalInd = np.where(np.amax(abs(intensidades))==abs(intensidades))
    izq=fundamentalInd[0][0]
    der = fundamentalInd[0][1]
    pintensidades = intensidades.copy()
    for i in range(100):
        pintensidades[izq + i] = 0.0
        pintensidades[izq - i] = 0.0
        pintensidades[der + i] = 0.0
        pintensidades[der - i] = 0.0
    return pintensidades

#Pasa bajas

def pasaBajas(frecuencias,intensidades):
    fundamentalInd = np.where(abs(frecuencias)>2000)
    pintensidades = intensidades.copy()
    for i in fundamentalInd[0]:
        pintensidades[i] = 0.0


    return pintensidades

#Pasa altas
def pasaAltas(frecuencias,intensidades):
    fundamentalInd = np.where(abs(frecuencias)<2000)
    pintensidades = intensidades.copy()
    for i in fundamentalInd[0]:
        pintensidades[i] = 0.0


    return pintensidades

#Pasa bandas
def pasaBandas(frecuencias, intensidades):
    aElim  = elimFundamental(frecuencias, intensidades)

    pintensidades = intensidades.copy()
    pintensidades = pintensidades-aElim
    return pintensidades

fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,sharey = True,sharex = True)
# fig(figsize = (10,10))
ax1.plot(xviolin,abs(yviolin),label="Violin normal",c = "b")
ax2.plot(xviolin,abs(elimFundamental(xviolin,yviolin)),label="Sin fundamental",c='g')
ax3.plot(xviolin,abs(pasaBajas(xviolin,yviolin)),label = "PasaBajas",c='r')
ax4.plot(xviolin,abs(pasaAltas(xviolin,yviolin)),label = "PasaAltas",c='black')
ax5.plot(xviolin,abs(pasaBandas(xviolin,yviolin)),label = "PasaBandas",c='orange')
ax1.set_title("Filtros",fontsize = 20)
ax5.set_xlabel(r"Frecuencia $(Hz)$")

ax1.set_ylabel("Amplitud")
ax2.set_ylabel("Amplitud")
ax3.set_ylabel("Amplitud")
ax4.set_ylabel("Amplitud")
ax5.set_ylabel("Amplitud")


ax1.set_xlim(-10000,10000)
ax2.set_xlim(-10000,10000)
ax3.set_xlim(-10000,10000)
ax4.set_xlim(-10000,10000)
ax5.set_xlim(-10000,10000)

ax1.set_ylim(0,600)
ax2.set_ylim(0,600)
ax3.set_ylim(0,600)
ax4.set_ylim(0,600)
ax5.set_ylim(0,600)

ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()
ax5.legend()

plt.savefig("ViolinFiltros.pdf")
# plt.show()
plt.close()


sinFund = elimFundamental(xviolin,yviolin)
pasaBajas = pasaBajas(xviolin,yviolin)
pasaAltas =(pasaAltas(xviolin,yviolin))
pasaBandas = (pasaBandas(xviolin,yviolin))




wav.write("violin_pico.wav", datViolin[0], ifft(sinFund).real)
wav.write("violin_pasabajos.wav", datViolin[0], ifft(pasaBajas).real)
wav.write("violin_pasaaltos.wav", datViolin[0], ifft(pasaAltas).real)
wav.write("violin_pasabanda.wav", datViolin[0], ifft(pasaBandas).real)
