#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite um ano qualquer meu camarada: '))

if ano % 4 == 0:
    print('Esse ano é BISSEXTO, que legal!')
else:
    print('Esse ano não é BISSEXTO, que chato!')