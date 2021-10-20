#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número para checar sua primalidade: '))
a = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m{}\033[m '.format(i), end='')
        a += 1


    else:
        print('\033[35m{}\033[m '.format(i), end='')

print('')
if a == 2:
    print('O seu número {} é um PRIMO!'.format(num))
else:
    print('O seu número {} NÃO é \033[35mPRIMO!\033[m'.format(num))