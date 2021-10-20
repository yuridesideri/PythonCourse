#Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


lista = []
count = 0
stop = True
run = True
n = 0
sum = 0
while run == stop:
    count += 1
    n = int(input('Digite um número qualquer '))
    cond = input('Você deseja continuar? [S/N]').lower()    
    if cond == 's': 
        run = True
    else:
        run = False
    sum = sum + n
    media = sum / count
    lista = lista + [n]
    
print('Você digitou {} números, a soma deles é {}, a média entre eles é {}. Sendo que o maior é {} e o menor é {}.'.format(count, sum, media, sorted(lista)[-1], sorted(lista)[0]))
