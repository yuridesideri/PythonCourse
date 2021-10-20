#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#C) Quais foram os números pares.

tupla = (int(input('Digite um número ')), int(input('Digite outro número ')), int(input('Mais um último número ')), int(input('Só mais um: ')))
print(tupla[:])
pares =[]
print(tupla.count(9))
if tupla[0] == 3 or tupla[1] == 3 or tupla[2] == 3 or tupla[3] == 3:
    print(tupla.index(3) + 1)
else:
    print('Não há nenhum 3')

for i in tupla:
    if i%2 == 0:
        print(f'{i} é par')
    
