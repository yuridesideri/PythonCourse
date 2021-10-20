#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

lista = []

def sorteia(lista):
    lista += [randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)]
    for v in lista:
        print(f'Sorteado o valor {v}')

def soma(n):
    soma = 0
    for v in n:
        if v % 2 == 0:
            soma += v

    print(f'A soma dos número pares é {soma}')



sorteia(lista)
soma(lista)























