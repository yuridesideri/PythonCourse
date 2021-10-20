#Aprimore o desafio 93 para que ele funcione com vários jogadores, 
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

cadastros = []

while True:
    #Init:
    rendimento = {}
    lista = []
    rendimento["nome"] = 0
    rendimento["partidas"] = 0
    rendimento["gols/partida"] = lista
    rendimento["total de gols"] = 0

    #Inputs:
    rendimento["nome"] = input('Digite o nome do Jogador: ')
    rendimento["partidas"] = int(input('Quantidade de partidas jogadas: '))
    for i in range(rendimento["partidas"]):
        lista.append(int(input(f'Digite a quantidade de gols da partida {i}: ')))
        rendimento["total de gols"] += lista[i]
    cadastros.append(rendimento.copy())


    #End loop:
    cont = input('Deseja continuar os cadastros? [S/N] ').lower()
    if cont in 'n':
        break

#Printer:
for f in cadastros:
    str = 'Next Player'
    print(f'{str:=^30}')

    print(f'Jogador {cadastros.index(f)}')
    for k, v in f.items():
        print(f'O {k} é {v} ')

    print('=-'* 15)

#After lookups:
while True:
    num = int(input('Deseja visualizar algum jogador? (Digite seu número) (999 SAIR)'))
    if num < 0 or num > len(cadastros) - 1 and num != 999:
        print('Esse número não existe')

    elif num == 999:
        break
        
    else:
        print('=-'* 15)
        print(f'Jogador {num}')
        for k, v in cadastros[num].items():
            print(f'O {k} é {v} ')
        print('=-'* 15)











