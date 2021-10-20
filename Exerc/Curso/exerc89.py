#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.



dados = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    lista = [nome, n1, n2]
    dados.append(lista)
    cont = input('Deseja continuar? [S/N]')
    if cont in 'Nn':
        break


for i, n in enumerate(dados):
    print(f'Aluno {i} é {dados[i][0]} com média {(dados[i][1] + dados[i][2]) / 2}')


while True:
    
    ind = int(input('Deseja ver as notas de algum aluno? [Digite o número dele] [999 para sair] '))
    if ind == 999:
        break
       
    print(f'O aluno {dados[ind][0]} tirou as notas {dados[ind][1]} e {dados[ind][2]}')





