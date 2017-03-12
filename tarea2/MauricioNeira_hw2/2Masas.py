import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

#inicializamosparametros
W1 = 10
W2 = 20
L = 8
L1 = 3
L2 = 4
L3 = 4
x1=0.0
x2=0.0
x3=0.0
x4=0.0
x5=0.0
x6=0.0
x7=0.0
x8=0.0
x9=0.0
umbral = 10**-3


def calcfs(x):
    fs = []
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    x5 = x[4]
    x6 = x[5]
    x7 = x[6]
    x8 = x[7]
    x9 = x[8]
    f1=L1*x4+L2*x5+L3*x6-L
    f2=L1*x1 + L2*x2 -L3*x3
    f3=x7*x1 - x8*x2 -W1
    f4=x7*x4 -x8*x5
    f5=x8*x2+x9*x3-W2
    f6=x8*x5-x9*x6
    f7=x1**2 + x4**2 -1
    f8=x2**2 +x5**2 -1
    f9=x3**2 + x6**2 -1
    fs.append(f1)
    fs.append(f2)
    fs.append(f3)
    fs.append(f4)
    fs.append(f5)
    fs.append(f6)
    fs.append(f7)
    fs.append(f8)
    fs.append(f9)
    fs = np.array(fs)
    return fs

def calcF(x):
    global F
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    x5 = x[4]
    x6 = x[5]
    x7 = x[6]
    x8 = x[7]
    x9 = x[8]
    F = np.array([[0.0 ,0.0 ,0.0 ,L1 ,L2 ,L3 ,0.0,0.0,0.0],
              [L1 ,L2 ,-1*L3,0.0 ,0.0 ,0.0 ,0.0,0.0,0.0],
              [x7  ,-x8 , 0.0,0.0 ,0.0 ,0.0 ,x1 ,-x2,0.0],
              [0.0 ,0.0 ,0.0 ,x7  ,-x8 ,0.0 ,x4 ,-x5,0.0],
              [0.0 ,x8  ,x9  ,0.0 ,0.0 ,0.0 ,0.0,x3 , x3],
              [0.0 ,0.0 ,0.0 ,0.0 ,x8  ,-x9 ,0.0,x5 ,-x6],
              [2*x1,0.0 ,0.0 ,2*x4,0.0 ,0.0 ,0.0,0.0,0.0],
              [0.0 ,2*x2,0.0 ,0.0 ,2*x5,0.0 ,0.0,0.0,0.0],
              [0.0 ,0.0 ,2*x3,0.0 ,0.0 ,2*x6,0.0,0.0,0.0]])
    return F

def NR(guess):
    global xs
    global F
    xs = guess
    thetas = [[np.arcsin(xs[0]),np.arcsin(xs[1]),np.arcsin(xs[2])]]
    ts = [[xs[6],xs[7],xs[8]]]
    xss=[]

    cont = 0
    xss.append(cont)
    cont+=1

    fs = calcfs(xs)
    F = calcF(xs)
    while(not paramos(fs)):
#         print(fs)
        dx = -1*linalg.solve(F,fs)
        xs += dx
        thetas.append([np.arcsin(xs[0]),np.arcsin(xs[1]),np.arcsin(xs[2])])
        ts.append([xs[6],xs[7],xs[8]])
        xss.append(cont)
        cont+=1
        fs = calcfs(xs)
        F = calcF(xs)

    thetas =np.array(thetas)
    ts = np.array(ts)
#     print(xss)
#     print(thetas)
    plt.figure(figsize=(10,10))
    plt.plot(xss,thetas[:,0],label = "Theta1")
    plt.plot(xss,thetas[:,1],label = "Theta2")
    plt.plot(xss,thetas[:,2],label = "Theta3")
    plt.ylabel("Angulo (rad)")
    plt.xlabel("Numero de iteracion ")
    plt.title("Convergencia de angulos",fontsize = 20)
    plt.legend(loc = "best")

    plt.savefig("AnglesPLOT.pdf")
    plt.figure(figsize=(10,10))
    plt.plot(xss,ts[:,0],label = "Tension 1")
    plt.plot(xss,ts[:,1],label = "Tension 2")
    plt.plot(xss,ts[:,2],label = "Tension 3")
    plt.ylabel("Tension (unidades arbitrarias)")
    plt.xlabel("Numero de iteracion ")
    plt.title("Convergencia de Tensiones",fontsize = 20)
    plt.legend(loc = "best")
    plt.savefig("TensionsPLOT.pdf")
    return xs
def paramos(fs):
    global umbral
    ans = True
    for i in fs:
        if abs(i)>umbral:
            ans = False
            break
    return ans

xs =NR([0.5,0.2,0.8,1,1,1,15,15,15])
xsReal = np.array([np.arcsin(xs[0]),np.arcsin(xs[1]),np.arcsin(xs[2]),
                  np.arccos(xs[3]),np.arccos(xs[4]),np.arccos(xs[5]),xs[6],xs[7],xs[8]])
print("Valores Obtenidos:")
print("")
print("    Theta1 = "+str(xsReal[0]))
print("    Theta2 = "+str(xsReal[1]))
print("    Theta3 = "+str(xsReal[2]))
print("        T1 = "+str(xs[6]))
print("        T2 = "+str(xs[7]))
print("        T3 = "+str(xs[8]))
