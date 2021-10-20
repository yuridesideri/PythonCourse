'''Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''


nasc = int(input('Informe seu ano de nascimento: '))
ano = 2021

if ano - nasc == 18:
    print('Você está em seu ano de alistamento militar')
if ano - nasc > 18:
    print('Você passou do prazo de alistamento. Dirija-se a um quartel IMEDIATAMENTE!')
else:
    print('Relaxa Gafanhoto! Você ainda não tem idade para se alistar. Mas deverá ir ao quartel daqui {} anos.'.format(18 - (2021 - nasc)))