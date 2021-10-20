#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna. 
# C) O maior valor da segunda linha.


c = 3 #colunas
l = 3 #linhas
matriz = []
colunas = []
pares = valterc =0 


for i in range(l):
    for n in range(c):
        add_e = int(input(f'Digite o elemento {i + 1}x{n + 1}: '))
        colunas.append(add_e)
        if add_e%2 == 0:
            pares += add_e
    matriz.append(colunas) 
    colunas = []


for i in range(l):
    valterc += matriz[i][2]
maior_seg = sorted(matriz[1])[-1]


#Gerador da Matriz:
print('Matriz:')
for i in range(l):
    for n in range(c):
        print(f'[{matriz[i][n]:^5}] ', end ='')
    print('')
print('=-'*20)




print(f'A soma de todos os valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {valterc}')
print(f'O maior valor da segunda linha é {maior_seg}')



