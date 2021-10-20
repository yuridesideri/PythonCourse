#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
n1 = random.randint(0, 5)
guess = int(input('Entre 0 a 5, qual número você acha que eu escolhi? '))
if n1 == guess :
    print('Parabéns o número realmente era o {}.'.format(guess))
else:
    print('Não foi desta vez. Eu escolhi o {}.'.format(n1))
