#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import random
lista = []
for i in range(0,7):
    lista = lista + [2021 - random.randint(1960,2021)]
    if lista[i] >= 18:
        print('A pessoa {} possui {} anos e já atingiu a MAIORIDADE!'.format(i + 1, lista[i]))
    else:
        print('A pessoa {} possui {} e ainda esta na MENORIDADE!'.format(i + 1, lista[i]))
print(lista)