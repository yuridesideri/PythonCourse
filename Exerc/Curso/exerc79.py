#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []

while True:
    num = int(input('Digite um número: '))
    if num in lista:
        print('O número já se encontra na lista...')
    else:
        print(f'Número {num} cadastrado com sucesso...')
        lista.append(num)
    key = input('Você deseja continuar? [S/N] ')
    if key in 'Nn':
        break

print(f'Aqui está a sua lista em ordem crescente: \n {sorted(lista)}')





