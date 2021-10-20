'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

import random
n1 = random.randint(0,50)
n2 = random.randint(0,50)
print('Meus valores escolhidos foram {} e {}.'.format(n1, n2))

if n1 > n2:
    print('O primeiro valor é maior')

elif n2 > n1: 
    print('O segundo valor é maior')
else:
    print('Os dois valores são iguais. Não há maior!')