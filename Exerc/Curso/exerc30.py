#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
import random, math

n1 = random.randint(0, 100)
ldig = int(list(str(n1))[-1])

if ldig == 2 or ldig == 4 or ldig == 6 or ldig == 8 or ldig == 0:
    print('O número que eu escolhi é o {} e esse número é PAR!'.format(n1))
else:
    print('O numero que eu escolhi é o {} e esse número é ÍMPAR!'.format(n1))
print(ldig)