#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
import random
lista = []
max = 5

for i in range(0,max):
    lista += [random.randint(40,120)]

cresc = sorted(lista)
print('O maior peso é {} e o menor peso é {}'.format(cresc[-1], cresc[0]))
