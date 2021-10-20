#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
val = int(input('Escolha um número para acessar sua tabuada! '))

for i in range(0,10):
    print(val * i)