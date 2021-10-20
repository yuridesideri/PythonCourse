#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#  No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = soma = 0

while True:
    choose = int(input('Digite um número inteiro: '))
    if choose == 999:
        break
    n += 1
    soma = soma + choose
print(f'Você digitou {n} números e a soma deles é {soma}')