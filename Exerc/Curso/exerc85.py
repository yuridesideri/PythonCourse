#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.

pares = []
impares = []
for i in range(0,7):
    num = int(input('Digite um valor: '))
    if num%2 == 0:
        pares.append(num)
    else:
        impares.append(num)


print(f'A lista dos pares é: {sorted(pares)}')
print(f'A lista dos impares é {sorted(impares)}')