''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER

'''


idade = 2021 - int(input('Qual o seu ano de nascimento? '))

if idade <= 9:
    print('A sua categoria é MIRIM')

elif 14 >= idade > 9:
    print('A sua categoria é INFANTIL')

elif 19 >= idade > 14:
    print('A sua categoria é JÚNIOR')

elif 25 >= idade > 9:
    print('A sua categoria é SÊNIOR')

else:
    print('A sua categoria é MASTER')