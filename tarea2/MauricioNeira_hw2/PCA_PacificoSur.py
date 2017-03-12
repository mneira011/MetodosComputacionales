import numpy as np
import matplotlib.pyplot as plt

d=np.genfromtxt("soiplaintext.txt",dtype=str,delimiter='\t',skip_header=1,skip_footer =1)
mes=[]
temp=[]
cont = 0;
for i in range(len(d)):
#     print(len(d[i].split(" ")))
    for j in range(13):
#         print(j)
        if((j!=0)and j!=" "):
            temp.append(d[i].split()[j])

for i in range(len(temp)):
    mes.append(i)

d1 = np.genfromtxt('heat_content_index.txt',skip_header=2,skip_footer=2)
t1 = d1[:,2]
t2 = d1[:,3]
t3 = d1[:,4]
plt.figure(figsize=(20,20))

plt.plot(mes[1236:],temp[1236:],alpha = 0.6,linewidth=4,label="SOI")
plt.ylabel(r"$SOI$",fontsize = 28)
plt.xlabel(r"$Tiempo\ (meses\ desde\ Enero\ de\ 1979)$",fontsize=28)
plt.legend(loc = 1,fontsize=21)
plt.twinx()
plt.plot(mes[1236:],t1,c='black',linewidth=2,label = "Temp. 130E-80W")
plt.plot(mes[1236:],t2,c='red',linewidth=2, label = "Temp. 160E-80W ")
plt.plot(mes[1236:],t3,c='orange',linewidth=2, label = "Temp. 180W-100W")

plt.ylabel(r"$Pormedio\ de\ anomalias\ en\ la\ temperatura\ (^\circ c)$",fontsize=28)
plt.legend(loc=2,fontsize=21)
plt.savefig("Anomalies_SOI_Plot.pdf")
data = [t1,t2,t3,temp[1236:]]
data = np.array(data).astype(np.float)
cov_matrix = np.cov(data)
values, vectors = np.linalg.eig(cov_matrix)

sumVals =sum(values)
values = values[0:2]
vectors = vectors[:,0:2]
print("El 1er componente tiene un valor de "+ str(values[0]) +
      " y tiene el vector " + str(vectors[:,0]))
print("Corresponde al " + str(100*values[0]/sumVals)+"% de la varianza")
print("El 2ndo componente tiene un valor de "+ str(values[1]) +
      " y tiene el vector " + str(vectors[:,1]))
print("Corresponde al " + str(100*values[1]/sumVals)+"% de la varianza")
new_data = np.dot(vectors.T, data)
# print(new_data)
plt.figure(figsize=(10,10))
plt.scatter(new_data[0,:], new_data[1,:])
plt.xlabel(r"$Componente\ principal\ 1$",fontsize = 15)
plt.ylabel(r"$Componente\ principal\ 2$",fontsize = 15)
plt.title(r"$PCA$",fontsize=20)
plt.savefig("PCA_Anomalies_SOI_Plot.pdf")
