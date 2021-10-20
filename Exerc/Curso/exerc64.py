#Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#  No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
count = 0
stop = False
run = False
n = 0
sum = 0
while run == stop:
    count += 1
    sum = sum + n
    n = int(input('Digite um número qualquer (999) para parar:'))
    if n == 999:
        run = True
print('Você digitou {} número e a soma deles é {}.'.format(count - 1, sum))
