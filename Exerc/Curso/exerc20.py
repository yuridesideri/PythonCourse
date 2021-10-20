#Dando shuffle na lista de variáveis


import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
nomes = [n1, n2, n3, n4]

random.shuffle(nomes)
print('A nova ordem de alunos é:')
print(nomes)