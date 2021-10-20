numero = int(input('Escolha um número: '))
n1 = numero % 10
n2 = numero // 10 % 10
n3 = numero // 100 % 10
n4 = numero // 1000 % 10




print('Seu número escolhido é {}'.format(numero))
print('O valor das unidades é: {}'.format(n1))
print('O valor das dezenas é: {}'.format(n2))
print('O valor das centenas é: {}'.format(n3))
print('O valor das unidades de milhar é: {}'.format(n4))