
# coding: utf-8

# In[649]:

import numpy as np
import matplotlib.pyplot as plt
import math



# In[650]:

def likelihood(y_obs, y_model):
    chi_squared = (1.0/2.0)*np.sum((y_obs-y_model)**2.0)/100
    return  np.exp(-chi_squared)


# In[651]:

def my_model(t, R, C):
    return 10*C*(1-np.exp(-t/(R*C)))


# In[652]:

data = np.loadtxt("CircuitoRC.txt")
t = data[:,0]
y = data[:,1]
ITERACIONES = 20000


# In[653]:

R_walk = np.zeros(ITERACIONES) #this is an empty list to keep all the steps
C_walk = np.zeros(ITERACIONES)
l_walk = np.zeros(ITERACIONES)

R_walk[0]= np.random.random()+10
C_walk[0]=  np.random.random()+10

y_init = my_model(t, R_walk[0], C_walk[0])
l_walk[0] = likelihood(y, y_init)


# In[654]:


for i in range(ITERACIONES-1):
    R_prime = np.random.normal(R_walk[i], 0.1)
    C_prime = np.random.normal(C_walk[i], 0.1)

    y_init = my_model(t, R_walk[i], C_walk[i])
    y_prime = my_model(t, R_prime, C_prime)

    l_prime = likelihood(y, y_prime)
    l_init = likelihood(y, y_init)
#     print(l_prime)
    alpha = l_prime/l_init
#     print(alpha)
    if(alpha>=1.0):
        R_walk[i+1]  = R_prime
        C_walk[i+1]  = C_prime
        l_walk[i+1] =  l_prime
    else:
        beta = np.random.uniform(0,1)
        if(beta<=alpha):
            R_walk[i+1]  = R_prime
            C_walk[i+1]  = C_prime
            l_walk[i+1] =  l_prime
        else:
            R_walk[i+1]  = R_walk[i]
            C_walk[i+1]  = C_walk[i]
            l_walk[i+1] =  l_init


# In[655]:

plt.figure(figsize = (7,7))

xmax = np.argmax(l_walk)
xmin = np.argmin(l_walk)
plt.xlim(l_walk[xmin],l_walk[xmax])
ymax = np.argmax(C_walk)
ymin = np.argmin(C_walk)
plt.ylim(C_walk[ymin],C_walk[ymax])
plt.scatter(l_walk,C_walk)
plt.xlabel(r"$Verosimilitud$",fontsize =15)
plt.ylabel(r"$C\ (F)$",fontsize =15)
plt.title("C en funcion de la verosimilitud",fontsize= 20)
plt.savefig("Cver.png")
plt.close()


# In[656]:

plt.figure(figsize = (7,7))
xmax = np.argmax(l_walk)
xmin = np.argmin(l_walk)
plt.xlim(l_walk[xmin],l_walk[xmax])
ymax = np.argmax(C_walk)
ymin = np.argmin(C_walk)
plt.ylim(R_walk[ymin],R_walk[ymax])
plt.scatter(l_walk,R_walk)
plt.xlabel(r"$Verosimilitud$",fontsize =15)
plt.ylabel(r"$R\ (\Omega)$",fontsize =15)
plt.title("R en funcion de la verosimilitud",fontsize= 20)
plt.savefig("Rver.png")
plt.close()


# In[657]:

ind = np.argmax(l_walk)

c = C_walk[ind]
r = R_walk[ind]


# In[ ]:




# In[659]:

plt.figure(figsize = (7,7))
count, bins, ignored =plt.hist(C_walk, 50, normed=True)
plt.xlabel(r"$Capacitancia\ (F)$",fontsize = 20)
plt.ylabel(r"$Frecuencia\ normalizada\ (F)$",fontsize = 20)
plt.title("Histograma C",fontsize=25)
plt.savefig("HistC.png")
plt.close()


# In[660]:

plt.figure(figsize = (7,7))
count, bins, ignored =plt.hist(R_walk, 50, normed=True)
plt.xlabel(r"$Resistencia\ (\Omega)$",fontsize = 20)
plt.ylabel(r"$Frecuencia\ normalizada\ (F)$",fontsize = 20)
plt.title("Histograma R",fontsize=25)
plt.savefig("HistR.png")
plt.close()


# In[661]:

plt.figure(figsize=(7,7))
plt.scatter(t,y,label = "Datos experimentales")
plt.plot(t,my_model(t, r, c),c='r',lw = 5,alpha =0.5,label=("R="+str(r)+" C="+str(c)))
plt.title("Parametros optimos",fontsize = 20)
plt.legend(loc=3)
plt.xlabel(r"$Tiempo$",fontsize=15)
plt.ylabel(r"$Carga\ (C)$",fontsize=15)
plt.savefig("ParamOptimos.png")
plt.close()


# In[ ]:
