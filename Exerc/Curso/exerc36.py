'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('=-' * 20)
print('ANALISADOR DE EMPRÉSTIMO BANCO INTER')
print('=-' * 20)

sal = int(input('Digite o valor do seu salário: '))
casa = int(input('Quanto você precisa para financiar a sua casa? '))
tempo = int(input('Em quantos meses você pretende pagar todo o empréstimo? '))
if casa /tempo > 0.3 * sal :
    print('Empréstimo NEGADO. Você não tem renda suficiente para esse financiamento!')
else:
    print('Empréstimo CONCEDIDO. Entre em contato com algum gestor do nosso Banco!')
