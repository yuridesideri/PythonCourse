#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
counter = 0
while True:

    cn = int(input('Escolha um número: '))
    cc = input('Par ou Ímpar? [P/I]')

    computern = random.randint(0,10)
    
    if (cn + computern)%2 == 1 and cc.lower() == 'p' or (cn + computern)%2 == 0 and cc.lower() == 'i':
        print(f'Desculpe! Você \033[31mPERDEU\033[m')    
        print(f'Eu escolhi {computern} e você escolheu {cn} totalizando {cn + computern}') 
        print(f'Atingiu um total de {counter} vitórias')
        break

    else:
        print(f'Muito Bem! Mais uma \033[32mVITÓRIA\033[m')    
        print(f'Eu escolhi {computern} e você escolheu {cn} totalizando {cn + computern}')

    counter += 1
