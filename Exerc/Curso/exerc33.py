''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
import random
n1 = str(random.randint(0,100))
n2 = str(random.randint(0,100))
n3 = str(random.randint(0,100))
print('Eu escolhi os números: {}, {} e {}.'.format(n1,n2,n3))

if n1 > n2 and n1 > n3:
    print('O maior número é' , n1)
    if n2 > n3:
        print('O menor número é' , n3)
    else:
        print('O menor número é' , n2)

        
if n2 > n3 and n2 > n3:
    print('O maior número é' , n2)
    if n3 > n1:
        print('O menor número é' , n1)
    else:
        print('O menor número é' , n3)


if n3 > n2 and n3 > n1:
    print('O maior número é' , n3)
    if n2 > n1:
        print('O menor número é' , n1)
    else:
        print('O menor número é' , n2)
