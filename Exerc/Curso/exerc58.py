import random
print('=-' * 20)
print('JOGO DE ADIVINHAÇÃO')
print('=-' * 20)

num = random.randint(0,10)
guess = 0
tries = 0

while guess != num:
    guess = int(input('Digite o valor que você acha que eu escolhi: (De 0 a 10) '))
    tries = tries + 1
    print('Não. Você errou. Tente NOVAMENTE!')

print('Parabéns. Agora sim!')
print('Você levou {} tentativas'.format(tries))