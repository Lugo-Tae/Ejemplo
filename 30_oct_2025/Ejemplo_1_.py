"""
Ejemplo 1 | Viernes 30 de Octubre 2025

Tema: Numpy I

Descripion: 

"""
#Operaciones matriciales

import numpy as np
import numpy.linalg as la 

M1 = [[1,8,9],[5,7,9],[6,4,2]]
M1 = [[7,9,5],[6,1,2],[3,8,9]]

print("Inversa de matriz")
print(la.inv(M1))

print("Determinante")
print(la.det(M1))

