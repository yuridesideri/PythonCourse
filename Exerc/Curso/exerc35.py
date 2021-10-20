''' Desenvolva um programa que leia o comprimento 
de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

import random
l1 = random.randint(1,20)
l2 = random.randint(1,20)
l3 = random.randint(1,20)

print('Para os segmentos de reta equivalente a {}, {} e {}'.format(l1, l2, l3))


maior = l1
resto = l2 + l3
if l2 >= l1 and l2 >= l3:
    maior = l2
    resto = l1 + l3
if l3 >= l1 and l3 >= l2:
    maior = l3
    resto = l1 + l2

if maior < resto:
    print('É possível criar um triângulo =)')
else:
    print('Não é possível criar um triângulo =(')
