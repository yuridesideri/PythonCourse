#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random, time, operator


data ={
'Jogador 1': random.randint(1,6),
'Jogador 2' : random.randint(1,6),
'Jogador 3' : random.randint(1,6),
'Jogador 4' : random.randint(1,6)
}


for k, v in data.items():
    print(f'O {k} tirou:  {v}')
    time.sleep(1)
print('=-' * 30)

organized = sorted(data.items(), key = operator.itemgetter(1), reverse=True)

for i, o in enumerate(organized):
    print(f'{i} {o[0]} {o[1]} ')









