import math
n=21
L=1.0
lista_x  []

for x in range(n):
    pos_x =  x * L/2.0/(n-1)
    y = math.sqrt(L/4*L-pos_x*pos_x)
    lista_x.append(pos_x)
print lista_x, y
