import random
import time
import numpy
import matplotlib.pyplot as plt
import scipy.interpolate as inter

lista = []
rozmiar = [10000, 30000, 500000, 10000000, 25000000, 30000000, 6000000, 70796500, 10000, 200000, 300000,330000, 400000, 422200,455100]

for x in range(len(rozmiar)):
    suma = 0
    start_time = time.time()
    for y in range(rozmiar[x]):
        suma += 1
    lista.append((rozmiar[x],time.time() - start_time))

dane_x = [x[0] for x in lista]
dane_y = [x[1] for x in lista]

f = inter.interp1d(dane_x, dane_y,fill_value="extrapolate")
x = numpy.linspace(0,70796500)
y = f(x)

plt.plot(dane_x,dane_y,linestyle='None', marker='+',markersize=20)
plt.plot(x,y)
plt.title('Czas vs Rozmiar')

plt.show()


    

    

