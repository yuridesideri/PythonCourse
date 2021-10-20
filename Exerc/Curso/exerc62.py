#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

a0 = int(input('Determine o primeiro termo da sua P.A.: '))
r = int(input('Defina a razão da sua P.A.: '))
c = 1
key = 11
while c < key:
    c += 1
    print('O Termo \033[34m{}\033[m é \033[31m{} \033[m'.format(c - 1,a0 ))
    a0 += r
    if c == key:
        key = int(input('Quantos números a mais você deseja mostrar? ' )) + c

print('Programa finalizado com sucesso!')