# Entidad: Universidad Sergio Arboleda
# Integrantes: Nicolás Cifuentes
# Profesor: Jonh Corredor Phd.
# Asignatura: Computación paralela y distribuida
# Tema: Prueba de rendimiento Cython

all:
		python3 setup.py build_ext --inplace
clean:
		rm -rf build *.so *.pyc *.c