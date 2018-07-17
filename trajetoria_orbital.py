import numpy as np
import pylab as pl

#Constantes
G = +1

#Condições iniciais

#Massas
m1 = 10000
m2 = 500 
m3 = 700

#Posições
x1 = 0.0
x2 = -100.0
x3 = 150
y1 = 0.0
y2 = 0.0
y3 = 0.0

#Velocidades
vx1 = 0.0
vx2 = 0.0
vx3 = 0.0
vy1 = 0.0
vy2 = -5.0
vy3 = 5.0

def f(r,t):

	#Recebendo os dados de posição e velocidade
	x1 = r[0]
	x2 = r[1]
	x3 = r[2]
	y1 = r[3]
	y2 = r[4]
	y3 = r[5]

	vx1 = r[6]
	vx2 = r[7]
	vx3 = r[8]
	vy1 = r[9]
	vy2 = r[10]
	vy3 = r[11]

	l12 = np.sqrt(((x2-x1)**2) + ((y2-y1)**2))
	l13 = np.sqrt(((x3-x1)**2) + ((y3-y1)**2))
	l23 = np.sqrt(((x3-x2)**2) + ((y3-y2)**2))

	fx1 = vx1
	fx2 = vx2
	fx3 = vx3
	fy1 = vy1
	fy2 = vy2
	fy3 = vy3

	fvx1 = ((G*m2*(x2-x1))/(l12**3) + (G*m3*(x3-x1)/(l13**3))) 
	fvx2 = ((G*m1*(x1-x2))/(l12**3) + (G*m3*(x3-x2)/(l23**3)))
	fvx3 = ((G*m1*(x1-x3))/(l13**3) + (G*m2*(x2-x3)/(l23**3)))

	fvy1 = ((G*m2*(y2-y1))/(l12**3) + (G*m3*(y3-y1)/(l13**3))) 
	fvy2 = ((G*m1*(y1-y2))/(l12**3) + (G*m3*(y3-y2)/(l23**3)))
	fvy3 = ((G*m1*(y1-y3))/(l13**3) + (G*m2*(y2-y3)/(l23**3)))

	return (np.array([fx1, fx2, fx3, fy1, fy2, fy3, fvx1, fvx2, fvx3, fvy1, fvy2, fvy3], float))


#Controles
a = 0.0
b = 200		#padrao 100
N = 10000
h = (b-a)/N

r = np.array([x1, x2, x3, y1, y2, y3, vx1, vx2, vx3, vy1, vy2, vy3], float)

#Lista de gravação de dados
pontstemp = np.arange(a,b,h)
posicaox1 = []
posicaox2 = []
posicaox3 = []
posicaoy1 = []
posicaoy2 = []
posicaoy3 = []
velocidx1 = []
velocidx2 = []
velocidx3 = []
velocidy1 = []
velocidy2 = []
velocidy3 = []

#Resolução das equações diferenciais com o método Runge-Kutta de quarta ordem
for t in pontstemp:
	posicaox1.append(r[0])
	posicaox2.append(r[1])
	posicaox3.append(r[2])
	posicaoy1.append(r[3])
	posicaoy2.append(r[4])
	posicaoy3.append(r[5])
	velocidx1.append(r[6])
	velocidx2.append(r[7])
	velocidx3.append(r[8])
	velocidy1.append(r[9])
	velocidy2.append(r[10])
	velocidy3.append(r[11])

	k1 = h*f(r,t)
	k2 = h*f(r+0.5*k1, t+0.5*h)
	k3 = h*f(r+0.5*k2, t+0.5*h)
	k4 = h*f(r+k3, t+h)
	r += (k1+2*k2+2*k3+k4)/6

	print(0.5*(t/len(pontstemp))*10000.0,"%")


#Preparando modo gráfico
#Realizando o modo gráfico
from vpython import sphere,canvas,color,vector,cylinder,box,helix,rate

#Configuração da janela
scene2 = canvas(title = "Simulação de órbitas caóticas", width = 600, height = 600,background=color.white)


esferabola1 = sphere(radius=7,pos=vector(x1,y1,0),color=color.yellow)
esferabola2 = sphere(radius=2,pos=vector(x2,y2,0),color=color.red)
esferabola3 = sphere(radius=2,pos=vector(x3,y3,0),color=color.blue)


cont = 0
T = len(pontstemp)
for k in range(T):

	esferabola1.pos = vector(posicaox1[k],posicaoy1[k],0.0)
	esferabola2.pos = vector(posicaox2[k],posicaoy2[k],0.0)
	esferabola3.pos = vector(posicaox3[k],posicaoy3[k],0.0)

	cont = cont + 1
	if (cont == 100):
		sphere(radius=1.0,pos=vector(posicaox2[k],posicaoy2[k],0),color=color.red)
		sphere(radius=1.0,pos=vector(posicaox3[k],posicaoy3[k],0),color=color.blue)
		cont = 0

	rate(N/100)
