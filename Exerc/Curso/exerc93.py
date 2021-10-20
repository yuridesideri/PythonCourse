#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

rendimento = {}
lista = []

rendimento["nome"] = 0
rendimento["partidas"] = 0
rendimento["gols/partida"] = lista

rendimento["total de gols"] = 0

rendimento["nome"] = input('Digite o nome do Jogador: ')
rendimento["partidas"] = int(input('Quantidade de partidas jogadas: '))

for i in range(rendimento["partidas"]):
    lista.append(int(input(f'Digite a quantidade de gols da partida {i}: ')))
    rendimento["total de gols"] += lista[i]




for k, v in rendimento.items():
    print(f'O {k} é {v} ')



