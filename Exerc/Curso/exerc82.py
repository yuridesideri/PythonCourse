#Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#  Ao final, mostre o conteúdo das três listas geradas.


lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num%2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    key = input('Deseja continuar? [S/N] ')
    if key in 'Nn':
        break


print(f'A lista total é: {lista}')
print(f'A lista dos pares é: {pares}')
print(f'A lista dos impares é {impares}')


