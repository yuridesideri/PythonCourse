'''  Exercício Python 34: Escreva um programa que pergunte o salário de
 um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, 
 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.  '''


import random

salario = random.randint(950, 1600)

print('Para o salário de R$', salario)

if salario > 1250:
    aumento = salario * 1.1

else:
    aumento = salario * 1.15

print('O aumento vai para R$', aumento)
