'''Crie um programa que faça o computador jogar Jokenpô com você.'''

import random

player = input('Escolha: Pedra, Papel ou Tesoura ')
print('Obs: o Default é Pedra')
pc = random.randint(1,3) 
choice = ['Tesoura', 'Papel', 'Pedra']
choice = choice[pc - 1]

print('{} vs {}'.format(player.upper(), choice.upper()))
if player.lower() == 'tesoura':
    player = 1

elif player.lower() ==  "papel" :
    player = 2

else:
    player = 3



if pc == player:
    print('Empatou')

elif pc == player + 1:
    print('Parabéns! Você Ganhou!')

elif pc == 1 and player == 3:
    print('Parabéns! Você Ganhou!')

else:
    print('Haha! Eu ganhei. Tente novamente!')

