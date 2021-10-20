#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da São Paulo.


times = ('Flamengo', 'Internacional', 'Altlético-MG', 'São Paulo', 
'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Ahtletico-PR', 'Bragantino',
 'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 
 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
 
num = times.index('São Paulo') + 1

print(f'Os 5 primeiros times são {times[0:6]}')
print(f'Os 4 últmos são {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'A posição do time São Paulo é a {num}')
