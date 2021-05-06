# Entidad: Universidad Sergio Arboleda
# Integrantes: Nicolás Cifuentes
# Profesor: Jonh Corredor Phd.
# Asignatura: Computación paralela y distribuida
# Tema: Prueba de rendimiento Cython

from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

exts=(cythonize('cyfunctionE.pyx'))
setup(ext_modules=exts, 
      include_dirs=[numpy.get_include()])
