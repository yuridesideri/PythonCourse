# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

cadastrados = []
mulheres = []
soma_idades = 0
acima = []

while True:
    dict = {}
    dict["nome"] = input('Digite o nome da pessoa: ')
    dict["sexo"] = input('Digite o sexo da pessoa: [M/F] ').lower()
    dict["idade"] = int(input('Digite o valor da idade da pessoa: '))
    cadastrados.append(dict.copy())

    soma_idades += dict["idade"]

    if dict["sexo"] in 'f':
        mulheres.append(dict["nome"])

    dict = {}
    cont = input('Deseja continuar os cadastros? [S/N] ').lower()
    if cont in 'n':
        break

idade_media = soma_idades / len(cadastrados)

print(f'A quantidade de pessoa cadastradas é {len(cadastrados)}')

print(f'A idade média é {idade_media}')

print('As mulheres são:')
for i, v in enumerate(mulheres):
    print(v)


for v in cadastrados:
    if v["idade"] > idade_media:
        acima.append(v["nome"])


print(f'As pessoas acima da média de idade são: {acima}')







