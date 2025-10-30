import math
import matplotlib.pyplot as plt

n = 100  # ejemplo, puedes cambiar n

# 1. Lista de valores de 1 en 1 hasta n
x = [x for x in range(1, n+1)]

# 2. Lista de valores de la función seno de 0 a 2π
#    Aquí hago 100 puntos igualmente espaciados
lista2 = [math.sin(x) for x in [i*2*math.pi/99 for i in range(100)]]

# 3. Lista de valores de x^2
lista3 = [x**2 for x in range(1, n+1)]

# 4. Lista de valores de 1/x

lista4 = [1/x for x in range(1, n+1)]

# 5. Lista de valores de 2x
lista5 = [2*x for x in range(1, n+1)]

fig, ax  = plt.subplots()
plt.plot(x,lista2)
plt.show()
