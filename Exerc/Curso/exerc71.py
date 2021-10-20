#Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS:

#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

valor = int(input('Digite o valor que você deseja sacar: '))

ced50 = valor // 50
ced20 = (valor-ced50 * 50) // 20
ced10 = (valor - (ced50 *50) - (ced20 * 20)) // 10
ced1 = (valor - (ced50 * 50) - (ced20 * 20) - (ced10 * 10)) // 1

print(f'Para o seu valor de {valor},você receberá:\n{ced50} cédulas de 50 Reais\n{ced20} cédulas de 20 Reais\n{ced10} cédulas de 10 Reais e \n{ced1} cédulas de 1 Real.')
