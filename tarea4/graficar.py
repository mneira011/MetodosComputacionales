import matplotlib.pyplot as plt
import numpy as np

def genGraph(nombre):
    data = np.loadtxt(nombre + ".dat",delimiter = ",")
    plt.figure( figsize=(6, 6))
    plt.imshow(data)

    plt.colorbar()
    plt.savefig(nombre+".png")


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
