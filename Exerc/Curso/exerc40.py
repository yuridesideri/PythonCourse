'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''


n1 = int(input('Digite sua nota 1: '))
n2 = int(input('Digite sua segunda nota: '))

m = (n1 + n2)/2

if m <= 5 :
    print('Você foi reprovado. Vai ter que repetir de ano!')


elif m >= 5 and m <= 6.9:
    print('Você passará por um processo de recuperação!')

else:
    print('Parabéns pelo seu esforço. Você está aprovado!')
