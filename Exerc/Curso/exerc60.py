#Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Escolha o seu número para descobrir o fatorial! '))
mult = 1

for i in range(1, num+1):
     mult = mult * i
    
print(mult)