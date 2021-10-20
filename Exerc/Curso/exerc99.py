#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    print(f'O maior número da lista é {max(num)}')



maior(1,4,2,7,8,2,3,4,51,7,8,3,100)


