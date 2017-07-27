import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle



def plotear(nombre):
    data = np.loadtxt(nombre+".txt")
    data1 = np.loadtxt(nombre+".dat")
    fig,ax = plt.subplots(1)
    ax.set_aspect('equal')
    plt.scatter(data[:,0],data[:,1])
    plt.scatter(data1[0], data1[1],c= 'r')
    circ = Circle((data1[0], data1[1]),data1[2],facecolor = 'none',edgecolor = 'r')
    ax.add_patch(circ)
    plt.xlabel(r"$Posicion\ en\ x\ (\AA)$",fontsize =15)
    plt.ylabel(r"$Posicion\ en\ y\ (\AA)$",fontsize =15)
    plt.title("Parametros: x = "+str(data1[0])+", y= "+str(data1[1])+" radio = "+str(data1[2]) , fontsize = 15)
    plt.savefig(nombre+".png")

plotear("Canal_ionico")
plotear("Canal_ionico1")
