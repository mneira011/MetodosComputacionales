import matplotlib.pyplot as plt
import numpy as np

# f = open("datos.dat")
data = np.loadtxt("datos.dat",delimiter = ",")
plt.figure( figsize=(6, 6))
plt.imshow(data)

plt.colorbar()
# plt.clim(50,100)
plt.savefig('tryout1.png')
