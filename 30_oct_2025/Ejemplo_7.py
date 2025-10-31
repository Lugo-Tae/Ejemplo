"""
Ejemplo 7 | Viernes 30 de Octubre 2025

Tema: Numpy II

Descripion: 

"""

import numpy as np
print("Arange")
print(np.arange(start = 1 ,stop = 15, step= 1, dtype = np.float32))
print("Linspace")
print(np.linspace(start = 1 ,stop = 15, num = 10,endpoint= False, dtype = np.float32))
print(np.linspace(start = 1 ,stop = 15, num = 10,endpoint= False, dtype = np.float32, retstep=True))
print("Logspace")
print(np.logspace(start = 1 ,stop = 4, num = 6, base = 2, endpoint= False))