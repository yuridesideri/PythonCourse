#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome = 'Null', gols = 'Null'):
    if nome == '':
        nome = 'Null'
    if gols == '':
        gols = 'Null'
    print('='* 50)
    print(f'O jogador {nome} fez {gols} gol(s)')
    print('='* 50)



ficha(input('Digite o nome do jogador: '), input('Digite a quantidade de gols que ele fez: '))








