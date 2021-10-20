#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    choice = int(input('Escolha um número para acessar a tabuada do respectivo: '))
    if choice < 0:
        break
    else:
        for i in range(0, 10):
            print(f'{choice} x {i} = {choice * i}')

print('O negativo não é aceito neste programa! Fim do Programa!')
