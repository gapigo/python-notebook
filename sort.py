from random import randint
from time import time

v = []
for i in range(1000000):
    v.append(randint(1, 50))

inicio = time()

# for i in range(len(v)):
#     for j in range(len(v)):
#         if v[j] > v[i]:             
#             aux = v[i]
#             v[i] = v[j]
#             v[j] = aux

v.sort()

print(f'{time() - inicio:.3f}s')
#print(v)