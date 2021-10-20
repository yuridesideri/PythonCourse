''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''

import random

preco = random.randint(1280, 2390)

print('O preço à vista no DINHEIRO/CHEQUE é {}'.format(preco * 0.9))

print('O preço à no cartão é de {}'.format(preco * 0.95))

print('O preço em até 2x é {}'.format(preco))

print('O preço a partir de 3x ou mais é de {}'.format(1.2 * preco))