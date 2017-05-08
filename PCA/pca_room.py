import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

with open("room-temperature.csv") as f:
    next(f)
    t1,t2,t3,t4= np.loadtxt(f,delimiter=',',usecols=(1,2,3,4) ,unpack=True)

ts =[]
for i in range(len(t1)):
    ts.append(i)

plt.figure(figsize=(15,15))
f, (ax1, ax2, ax3,ax4) = plt.subplots(4, sharex=True, sharey=True)
ax1.plot(ts, t1)
ax1.set_title('Temperatura vs tiempo')
ax2.plot(ts, t2)
ax3.plot(ts,t3)
ax4.plot(ts,t4)
# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
plt.xlabel("Tiempo")
ax2.set_ylabel("Temperatura")
f.subplots_adjust(hspace=0)
plt.savefig("room.pdf")

t1p = sum(t1)/len(t1)
t2p = sum(t2)/len(t1)
t3p = sum(t3)/len(t1)
t4p = sum(t4)/len(t1)
t1std = np.std(t1)
t2std = np.std(t2)
t3std = np.std(t3)
t4std = np.std(t4)

t1 = (t1- t1p)/t1std
t2 = (t2- t2p)/t2std
t3 = (t3- t3p)/t3std
t4 = (t4- t4p)/t4std

data = []
data.append(t1)
data.append(t2)
data.append(t3)
data.append(t4)
data = np.array(data)

cov_matrix = np.cov(data)
print("La matriz de covarianza es:")
print(cov_matrix)

values, vectors = np.linalg.eig(cov_matrix)
sumvar = sum(values)
values=values[:2]
vectors = vectors[:,:2]

print("La primera componente principal es "+ str(vectors.T[0])+" con el valor "+str(values[0]))
print("La segunda componente principal es "+ str(vectors.T[1])+" con el valor "+str(values[1]))

print("La primera componente principal explica el "+ str(values[0]/sumvar)+ " % de la varianza.")
print("La segunda componente principal explica el "+ str(values[1]/sumvar)+ " % de la varianza.")

plt.figure(figsize = (10,10))
xmin = min(t2)
xmax = max(t2)
xs = np.linspace(xmin,xmax,1000)
m1 = vectors.T[0][0]/vectors.T[0][1]
m2 = vectors.T[1][0]/vectors.T[1][1]
plt.scatter(t2,t1)
plt.plot(xs,m1*xs)
plt.plot(xs,m2*xs)
plt.xlabel("Temp Front Right")
plt.ylabel("Temp Front Left")
plt.title("Front right vs front left")
plt.savefig("pca_fr_fl.pdf")


plt.figure(figsize = (10,10))
xmin = min(t2)
xmax = max(t2)
xs = np.linspace(xmin,xmax,1000)
m1 = vectors.T[0][0]/vectors.T[0][2]
m2 = vectors.T[1][0]/vectors.T[1][2]

plt.plot(xs,m1*xs)
plt.plot(xs,m2*xs)
plt.scatter(t3,t1)
plt.xlabel("Temp Back Left")
plt.ylabel("Temp Front Left")
plt.title("Back left vs front left")
plt.savefig("pca_bl_fl.pdf")


