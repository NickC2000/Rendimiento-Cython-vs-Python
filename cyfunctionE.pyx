# Entidad: Universidad Sergio Arboleda
# Integrantes: Nicolás Cifuentes
# Profesor: Jonh Corredor Phd.
# Asignatura: Computación paralela y distribuida
# Tema: Prueba de rendimiento Cython

#cython: language_level=3

cimport cython
cimport numpy as np
import numpy as np
from cython.parallel import prange

cdef extern from 'math.h':
        double exp(double x) nogil

def rbf_network(np.ndarray[np.float_t, ndim=2] X, np.ndarray[np.float_t, ndim=1]  beta, int theta):

    cdef int N = X.shape[0]
    cdef int D = X.shape[1]
    cdef np.ndarray[np.float_t, ndim=1] Y = np.zeros(N)

    cdef int i,j 
    cdef float r 

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y