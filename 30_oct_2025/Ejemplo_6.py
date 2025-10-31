"""
Ejemplo 6 | Viernes 30 de Octubre 2025

Tema: Numpy II

Descripion: 

"""
# Rangos numericos

import numpy as np

print("Matriz")
print(np.full(shape = (2,3), fill_value = 3.5))
print(np.full((2,3),3.5))

A = np.array([1,2,3,4])
print("Diagonal principal")
print(np.diag(A))

print(np.tri(M=5, N=6, k=0))