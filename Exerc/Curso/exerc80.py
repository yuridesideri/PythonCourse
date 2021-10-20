#Crie um programa onde o usuário possa digitar cinco valores numéricos 
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#  No final, mostre a lista ordenada na tela.


lista = []
for i in range(0,5):
    val = int(input('Digite um valor numérico: '))
    for count, n in enumerate(lista):
        if val < n:
            lista.insert(count, val)
            break
        else:
            lista.append(val)
            break
    if lista == []:
        lista.append(val)
print(lista)




