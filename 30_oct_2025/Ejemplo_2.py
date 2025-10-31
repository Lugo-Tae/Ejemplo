"""
Ejemplo 2 | Viernes 30 de Octubre 2025

Tema: Numpy1

Descripion: 

"""

# Operaciones estadisticca basicas

import numpy as np
import numpy.linalg as la

A = [1,8,9,15,11,2,3]
A = np.array(A)

M1 = [[1,7,8],[2,6,4],[2,6,7]]
M1 = np. matrix(M1)

# Arreglo

print("Operaciones de arreglos")
print(np.mean(A))
print(np.median(A))
print(np.std(A))
print(np.var(A))
print("")

# Matriz

print("Operaciones de matrices")
print(np.mean(M1))
print(np.median(M1))
print(np.std(M1))
print(np.var(M1))
print("")

# operaciones basicas numpy

print("Operaciones basicas arreglo")

print(np.sum(A))
print(np.prod(A))
print(np.max(M1))
print(np.min(A))
print("")

print("Operaciones basicas matrices")

print(np.sum(M1))
print(np.prod(M1))
print(np.max(M1))
print(np.min(M1))
print("")