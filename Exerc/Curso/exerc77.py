#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('Olho', 'Computador', 'Tablet', 'Celular', 'Estojo', 'Casa', 'Televisão')
vogais = []
for i in range(len(tupla)):

    for n in tupla[i]:
        if n in 'AEIOUaeiou':
            vogais += n


    print(f'A palavra {tupla[i]} possui {vogais} como respectivas vogais')
    vogais = []