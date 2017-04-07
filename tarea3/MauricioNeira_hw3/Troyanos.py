import numpy as np
import matplotlib.pyplot as plt

class Planeta:
    Fx = 0.0
    Fy = 0.0
    Fz = 0.0
    xpre = 0.0
    ypre = 0.0
    zpre = 0.0
    vxpre = 0.0
    vypre = 0.0
    vzpre = 0.0
    preFx = 0.0
    preFy = 0.0
    preFz = 0.0

    def __init__(self,masa, x,y,z,vx,vy,vz):
        self.masa = masa
        self.prex = x
        self.prey = y
        self.prez = z
        self.prevx = vx
        self.prevy = vy
        self.prevz = vz

    def precalcFs(self,planeta2):
        dx = planeta2.prex - self.prex
        dy= planeta2.prey - self.prey
        dz= planeta2.prez - self.prez
        #G=6.67408E-11 --- en el enunciado dice considerarlo = 1
        phi= planeta2.masa*self.masa*(1)/(dx**2.0+dy**2.0+dz**2.0)
        rx = dx/((dx**2.0+dy**2.0+dz**2.0)**0.5)
        ry = dy/((dx**2.0+dy**2.0+dz**2.0)**0.5)
        rz = dz/((dx**2.0+dy**2.0+dz**2.0)**0.5)
        self.preFx = phi*rx+self.preFx
        self.preFy = phi*ry+self.preFy
        self.preFz = phi*rz+self.preFz

    def calcFs(self ,planeta2):

        dx = planeta2.x - self.x
        dy= planeta2.y - self.y
        dz= planeta2.z - self.z
        #G=6.67408E-11 --- en el enunciado dice considerarlo = 1
        phi= planeta2.masa*self.masa*(1)/(dx**2.0+dy**2.0+dz**2.0)
        rx = dx/((dx**2.0+dy**2.0+dz**2.0)**0.5)
        ry = dy/((dx**2.0+dy**2.0+dz**2.0)**0.5)
        rz = dz/((dx**2.0+dy**2.0+dz**2.0)**0.5)
        self.Fx = phi*rx+self.Fx
        self.Fy = phi*ry+self.Fy
        self.Fz = phi*rz+self.Fz
    def resetFs(self):
        self.Fx = 0
        self.Fy = 0
        self.Fz = 0
    def preleap(self,h):
        self.vx= self.prevx + h*self.preFx/self.masa
        self.vy= self.prevy + h*self.preFy/self.masa
        self.vz= self.prevz + h*self.preFz/self.masa
        self.x = self.prex +h*self.vx
        self.y = self.prey +h*self.vy
        self.z = self.prez +h*self.vz
    def leap(self,h):

        vxmed = self.vx + 0.5*h*self.Fx/self.masa
        vymed = self.vy + 0.5*h*self.Fy/self.masa
        vzmed = self.vz + 0.5*h*self.Fz/self.masa

        self.x = self.x + vxmed*h
        self.y = self.y + vymed*h
        self.z = self.z + vzmed*h

        self.vx = vxmed + 0.5*h*self.Fx/self.masa
        self.vy = vymed + 0.5*h*self.Fy/self.masa
        self.vz = vzmed + 0.5*h*self.Fz/self.masa

r1 = -100.0/1048
m1 = 1047.0
m2 = 1.0
r2 = 100.0-100.0/1048
vpy = abs(r2)*(abs((m1+m2)/(r2+r1)**3.0))**0.5
vey = -1*abs(r1)*(abs((m1+m2)/(r1+r2)**3.0))**0.5



estrella = Planeta(m1,r1,0,0,0,vey,0)
planeta = Planeta(m2,r2,0,0,0,vpy,0)
troyano = Planeta(0.005,np.cos(60*np.pi/180)*r2,np.sin(60*np.pi/180)*r2,0,-1*vpy*np.sin(60*np.pi/180),vpy*np.cos(60*np.pi/180),0)

xs= []
ys = []
xs1 = []
ys1 = []
xs2 = []
ys2=[]

xs.append(planeta.prex)
ys.append(planeta.prey)

xs1.append(estrella.prex)
ys1.append(estrella.prey)

xs2.append(troyano.prex)
ys2.append(troyano.prey)

planeta.resetFs()
estrella.resetFs()
troyano.resetFs()

estrella.precalcFs(planeta)
estrella.precalcFs(troyano)

planeta.precalcFs(estrella)
planeta.precalcFs(troyano)

troyano.precalcFs(planeta)
troyano.precalcFs(estrella)

estrella.preleap(0.01)
planeta.preleap(0.01)
troyano.preleap(0.01)

xs.append(planeta.x)
ys.append(planeta.y)

xs1.append(estrella.x)
ys1.append(estrella.y)

xs2.append(troyano.x)
ys2.append(troyano.y)

for i in range(40000):

    planeta.resetFs()
    estrella.resetFs()
    troyano.resetFs()

    estrella.calcFs(planeta)
    estrella.calcFs(troyano)

    planeta.calcFs(estrella)
    planeta.calcFs(troyano)

    troyano.calcFs(planeta)
    troyano.calcFs(estrella)

    planeta.leap(0.01)
    estrella.leap(0.01)
    troyano.leap(0.01)

    xs.append(planeta.x)
    ys.append(planeta.y)
    xs1.append(estrella.x)
    ys1.append(estrella.y)
    xs2.append(troyano.x)
    ys2.append(troyano.y)



fig, (ax1,ax2,ax3) = plt.subplots(3)

fig.set_figheight(12)
fig.set_figwidth(6)
# fig(figsize=(10,10))
ax1.plot(xs,ys,label="Planeta",c = "black")
ax2.plot(xs1,ys1,label="Estrella",c="orange")
ax3.plot(xs2,ys2,label="Troyano",c='red')
ax1.set_title("Trayectorias",fontsize = 20)
ax3.set_xlabel(r"x $(und. arbitrairas)$")
ax1.set_ylabel("y $(und. arbitrairas)$")
ax2.set_ylabel("y $(und. arbitrairas)$")
ax3.set_ylabel("y $(und. arbitrairas)$")

ax2.set_xlim(-0.1,0.1)
ax2.set_ylim(-0.1,0.1)
# ax1.set_xlim(-10000,10000)
ax1.legend()
ax2.legend()
ax3.legend()

plt.savefig("OrbitsPLOT.pdf")
plt.close()



def solve(estrella,planeta,troyano):
    xs= []
    ys = []
    xs1 = []
    ys1 = []
    xs2 = []
    ys2=[]

    xs.append(planeta.prex)
    ys.append(planeta.prey)

    xs1.append(estrella.prex)
    ys1.append(estrella.prey)

    xs2.append(troyano.prex)
    ys2.append(troyano.prey)

    planeta.resetFs()
    estrella.resetFs()
    troyano.resetFs()

    estrella.precalcFs(planeta)
    estrella.precalcFs(troyano)

    planeta.precalcFs(estrella)
    planeta.precalcFs(troyano)

    troyano.precalcFs(planeta)
    troyano.precalcFs(estrella)

    estrella.preleap(0.01)
    planeta.preleap(0.01)
    troyano.preleap(0.01)

    xs.append(planeta.x)
    ys.append(planeta.y)

    xs1.append(estrella.x)
    ys1.append(estrella.y)

    xs2.append(troyano.x)
    ys2.append(troyano.y)

    for i in range(40000):

        planeta.resetFs()
        estrella.resetFs()
        troyano.resetFs()

        estrella.calcFs(planeta)
        estrella.calcFs(troyano)

        planeta.calcFs(estrella)
        planeta.calcFs(troyano)

        troyano.calcFs(planeta)
        troyano.calcFs(estrella)

        planeta.leap(0.01)
        estrella.leap(0.01)
        troyano.leap(0.01)

        xs.append(planeta.x)
        ys.append(planeta.y)
        xs1.append(estrella.x)
        ys1.append(estrella.y)
        xs2.append(troyano.x)
        ys2.append(troyano.y)
    xs= np.array(xs)
    ys = np.array(ys)
    xs1 = np.array(xs1)
    ys1 = np.array(ys1)
    xs2 = np.array(xs2)
    ys2= np.array(ys2)
    return xs, ys,xs1, ys1, xs2, ys2

def cordRelativas(planetax,planetay,troyanox,troyanoy):
    ansx = troyanox-planetax
    ansy = troyanoy-planetay
    return ansx,ansy

def inicializar(despx,despy,despvx,despvy,pm2):
    r1 = -100.0/1048
    m1 = 1047.0
    m2 = pm2#1.0
    r2 = 100.0-100.0/1048
    vpy = abs(r2)*(abs((m1+m2)/(r2+r1)**3.0))**0.5
    vey = -1*abs(r1)*(abs((m1+m2)/(r1+r2)**3.0))**0.5



    estrella = Planeta(m1,r1,0,0,0,vey,0)
    planeta = Planeta(m2,r2,0,0,0,vpy,0)
    troyano = Planeta(0.005,np.cos(60*np.pi/180)*r2+despx,np.sin(60*np.pi/180)*r2+despy,0,-1*vpy*np.sin(60*np.pi/180)+despx,vpy*np.cos(60*np.pi/180)+despy,0)
    return estrella,planeta,troyano

plt.figure(figsize = (7,7))
for i in range(0,4,1):
    estrella,planeta,troyano = inicializar(i,i,0,0,1)
    planetax, planetay,estrellax, estrellay, troyanox, troyanoy = solve(estrella,planeta,troyano)
    relatx,relaty = cordRelativas(planetax,planetay,troyanox,troyanoy)
    plt.plot(relatx,relaty,label="Despl. x y y ="+str(i))
plt.legend(loc="best")
plt.xlabel("x troyano relat. a planeta (unid. arb.)")
plt.ylabel("y troyano relat. a planeta (unid. arb.)")
plt.title("Pertr. cond. iniciales",fontsize = 20)
plt.savefig("Troyano.pdf")
plt.close()



fig, (ax1,ax2,ax3,ax4) = plt.subplots(4)

fig.set_figheight(17)
fig.set_figwidth(7)



estrella,planeta,troyano = inicializar(0,0,0,0,10)
planetax, planetay,estrellax, estrellay, troyanox, troyanoy = solve(estrella,planeta,troyano)
ax1.plot(troyanox,troyanoy,label="m2="+str(10),c = "black")

estrella,planeta,troyano = inicializar(0,0,0,0,20)
planetax, planetay,estrellax, estrellay, troyanox, troyanoy = solve(estrella,planeta,troyano)
ax2.plot(troyanox,troyanoy,label="m2="+str(20),c="orange")

estrella,planeta,troyano = inicializar(0,0,0,0,30)
planetax, planetay,estrellax, estrellay, troyanox, troyanoy = solve(estrella,planeta,troyano)
ax3.plot(troyanox,troyanoy,label="m2="+str(30),c='red')


estrella,planeta,troyano = inicializar(0,0,0,0,40)
planetax, planetay,estrellax, estrellay, troyanox, troyanoy = solve(estrella,planeta,troyano)
ax4.plot(troyanox,troyanoy,label="m2="+str(40),c='blue')


ax1.set_title("Trayectorias del Troy.",fontsize = 20)
ax4.set_xlabel(r"x $(und. arbitrairas)$")
ax1.set_ylabel("y $(und. arbitrairas)$")
ax2.set_ylabel("y $(und. arbitrairas)$")
ax3.set_ylabel("y $(und. arbitrairas)$")
ax4.set_ylabel("y $(und. arbitrairas)$")


ax1.legend(loc="best")
ax2.legend(loc="best")
ax3.legend(loc="best")
ax4.legend(loc="best")
# plt.show()
plt.savefig("MassPLOT.pdf")
plt.close()
