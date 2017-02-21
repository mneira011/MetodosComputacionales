import numpy as np
import matplotlib.pyplot as plt

Arad,Prad,VGas,VDisk,VBul,Vel,e_Vel = np.loadtxt("RotationCurve_F571-8.txt",delimiter=' ', usecols=(0, 1,2,3,4,5,6), unpack=True)
plt.scatter(Prad,Vel,c='black', label = "Vel")
plt.scatter(Prad,VGas+VDisk+VBul,c='g',label = "VGas+VDisk+VBul")
plt.xlabel(r"$Radio\ (kpc)$",fontsize = 15)
plt.ylabel(r"$Velocidad\ (km/s)$",fontsize = 15)
plt.title(r"$Velocidad\ vs\ Radio$",fontsize = 30)
plt.legend(loc = 4)
plt.savefig("RotationCurvePlot.pdf")
