#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#  Ex: n = leiaInt(‘Digite um n: ‘)


def leiaint(a):
    while True:
        if input(a).isnumeric() == True:
            break
        else:
            print('Um valor NÚMERICO por favor!')
    return int(a)
        



leiaint('Digite um número: ')







