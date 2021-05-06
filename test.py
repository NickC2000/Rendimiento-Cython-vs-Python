# Entidad: Universidad Sergio Arboleda
# Integrantes: Nicolás Cifuentes
# Profesor: Jonh Corredor Phd.
# Asignatura: Computación paralela y distribuida
# Tema: Prueba de rendimiento Cython

from cyfunctionE import rbf_network
import numpy as np
import functionE
import time
import numpy as np
import matplotlib.pyplot as plt

D = 5
N = 1500
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10

inicio = time.time()
functionE.rbf_network(X, beta, theta)
tiempoPy = time.time() - inicio

inicio = time.time()
rbf_network(X, beta, theta)
tiempoCy = time.time() - inicio

speedUp = round(tiempoPy/tiempoCy,3)

print('Tiempo python: {} \nTiempo Cython: {} \nSpeedUp: {}'.format(tiempoPy,tiempoCy,speedUp))

tiempos = [tiempoPy,tiempoCy]
labels = ['Python','Cython']
plt.barh(labels,tiempos,align='center',alpha=0.5,color=['blue','green'])
plt.title('Rendimiento Cython vs Python')
plt.xlabel('Tiempo')
plt.savefig('rendimiento.png')
plt.show()