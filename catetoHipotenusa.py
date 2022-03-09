# faça um programa que leia o cumprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#caucule e mostre o cumprimento da hipotenusa.

import math
co = float(input('valor do cateto oposto'))
ca = float(input('valor do cateto adjacente'))
hi = math.hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'. format(hi))

#pode-se fazer de forma matemática
#co = float(input('valor do cateto oposto'))
#ca = float(input('valor do cateto adjacente'))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('a hipotenusa vai medir {} '. format(hi))