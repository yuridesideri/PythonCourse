#Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas.                                                                                                                
#B) Uma listagem com as pessoas mais pesadas.                                                                                                    
#C) Uma listagem com as pessoas mais leves.


nomes = []
pesos = []

while True:
    print('=-'*20)
    print('CADASTROS')
    print('=-'*20)
    nome = input('Digite um nome: ')
    peso = int(input('Digite um peso: '))
    nomes.append(nome)
    pesos.append(peso)
    key = input('Deseja Finalizar? [S/N] ')
    if key in 'Ss':
        break

print(f'Foram cadastradas {len(nomes)} pessoas.')
print(f'A pessoa mais pesada é a {nomes[pesos.index(sorted(pesos)[-1])]}')
print(f'A pessoa mais leve é a {nomes[pesos.index(sorted(pesos)[0])]}')

