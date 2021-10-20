#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

val = []
for i in range(0,5):
    ac = int(input('Digite um valor numérico: '))

    val.append(ac)
sort = sorted(val)
print(f'O menor valor foi {sort[0]} na posição {val.index(sort[0])} e o maior valor foi {sort[-1]} na posição {val.index(sort[-1])}.')


