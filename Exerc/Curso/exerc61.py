#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

a0 = int(input('Determine o primeiro termo da sua P.A.: '))
r = int(input('Defina a razão da sua P.A.: '))
c = 1
while c <= 10:
    c += 1
    print('O Termo \033[34m{}\033[m é \033[31m{} \033[m'.format(c - 1,a0 ))
    a0 += r