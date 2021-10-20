#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random

lista = []
p = []


msg = 'GANHADOR DE MEGA SENA'
print('=-'*20)
print(f'{msg:^40}')
print('=-'*20)


jogos = int(input('Digite quantos jogos você quer criar: '))

for i in range(jogos):
    for j in range(6):
        e = random.randint(1,60)
        p.append(e)

    lista.append(p)
    print(f'O jogo {i + 1} é {p}')
    p = []



    

