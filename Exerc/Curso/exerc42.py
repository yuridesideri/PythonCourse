import random

l1 = random.randint(1,20)
l2 = random.randint(1,20)
l3 = random.randint(1,20)
print('Eu usei as medidas {}, {} e {}'.format(l1, l2, l3))

if l1 > l2 and l1 > l3:
    maior = l1
    soma = l2 + l3

elif l2 > l1 and l2 > l3:
    maior = l2
    soma = l1 + l3

else:
    maior = l3
    soma = l1 + l2



if maior < soma:
    if l1 == l2 or l2 == l3 or l3 == l1:
        if l1 == l2 == l3:
            print('Seu triângulo é equilátero')
        else:
            print('Seu triângulo é isósceles')
    else:
        print('Seu triângulo é escaleno')

else: 
    print('Impossível formar um triângulo com essa medidas!')