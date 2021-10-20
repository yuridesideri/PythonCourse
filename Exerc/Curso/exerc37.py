'''Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal.'''


num = int(input('Digite um número para fazer a conversão: '))
print( '''Digite:
[1] para BINÁRIO, 
[2] para OCTAL e   
[3] para HEXADECIMAL.''')
key = int(input())

if key == 1:
    print('Seu número em BINÁRIO é {}'.format(str(bin(num))[2:]))

elif key == 2:
    print('Seu número em {} é {}'.format('OCTADECIMAL', str(oct(num))[2:]))

else:
    print('Seu número em {} é {}'.format('HEXADECIMAL', str(hex(num))[2:]))