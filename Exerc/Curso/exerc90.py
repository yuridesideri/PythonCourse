# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

nome = input('Digite o nome do aluno:')
média = int(input('Digite a média do aluno: '))
if média >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

info = {'nome' : nome , 'média' : média, 'situação' : situacao}

print(f'O aluno é {info["nome"]}\nSua média é {info["média"]}\nE ele(a) foi {info["situação"]}')

