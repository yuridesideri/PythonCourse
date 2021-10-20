#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

import random
quantidade_de_pessoas = 196
nomesf = ['Rafaela', 'Jenifer', 'Claudete', 'Cinderela', 'Aline', 'Maria', 'Adelaine']
nomesm = ['João', 'Cleitinho', 'Carlos', 'Juca', 'Gabriel', 'Afonso', 'Lucas', 'Marinel']
idadem = homens = idadef = mulheres = jovens = []
soma = 0



for i in range(0,quantidade_de_pessoas):
    key = random.randint(0,1)
    pessoa = [random.choice(nomesm) if key == 1 else random.choice(nomesf)]
    idade = random.randint(5,85)
    sexo = 'M' if key == 1 else 'F'
    if key == 1:
        idadem = idadem + [idade]
        homens = homens + [pessoa]
    else:
        idadef = idadef + [idade]
        mulheres = mulheres + [pessoa]
        if idade < 20:
            jovens = jovens + [pessoa]

totalidade = idadef + idadem

for n in range(0, quantidade_de_pessoas):
    soma = soma + int(totalidade[n])

mediaidade = soma/quantidade_de_pessoas ## 1 Problema Comcluído!

if len(homens) > 0:
    homem_mais_velho = homens[idadem.index(int(sorted(idadem)[-1]))] ## 2 Problema Concluído!
else:
    homem_mais_velho = 'Ausente'


qntd_jovens = len(jovens)   #3 Problema Concluído


print('A média das idades dos participantes é de {}'.format(mediaidade))
print('O homem mais velho é o {}'.format(homem_mais_velho))
print('A quantidade de mulheres abaixo de 20 anos de idade é {}'.format(qntd_jovens))








