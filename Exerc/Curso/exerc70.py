#Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não.
#  No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.
lista = []
maiorque1000 = total = 0

while True:
    print('=-' * 20)
    nome = input('Digite o nome do seu produto: ')
    preço = float(input('Digite o preço desse produto: '))
    print('=-' * 20)
    lista += [preço]
    total = total + preço
    if preço > 1000:
        maiorque1000 += 1
    
    if sorted(lista)[0] == preço:
        mais_barato = nome


    cont = input('Você deseja continuar? [S/N] ')
    if cont in 'Nn':
        break

print(f'O total gasto com essas compras é R$ {total:.2f}')
print(f'{maiorque1000} produtos custam mais que R$ 1000,00')
print(f'O produto mais barato é o {mais_barato}')

    
