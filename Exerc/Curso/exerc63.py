#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

#0 – 1 – 1 – 2 – 3 – 5 – 8


n = int(input('Quantos números Fibonacci você deseja visualizar? '))

a0 = 0
a1 = 1
run = 0
while run < n:
    print(a0)
    run += 1

    store = a0 

    a0 = a1

    a1 += store

print('Programa finalizado')
