#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = input('Quantos Quilômetros tem a sua viagem? ')
if km <= 200:
    print('O total a pagar por essa viagem é R$ {}'.format(km* 0.5))
else:
    print('O total a pagar por essa viagem é R$ {}'.format(km* 0.45))