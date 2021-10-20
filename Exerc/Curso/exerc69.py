#Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.

mulher_menor = homens = maior18 = 0
while True:
    print('=-' * 20)
    idade = int(input('Digite a idade desta pessoa: '))
    sexo = input('Digite o sexo dessa pessoa [M/F] ')
    print('=-' * 20)
    if sexo.lower() == 'f' and idade < 20:
        mulher_menor += 1
    
    if sexo.lower() == 'm':
        homens += 1

    if idade > 18:
        maior18 += 1

    cont = input('Deseja continuar a colocar pessoas? [S/N] ')
    if cont in 'Nn':
        break
print('Fim do \033[32mPROGRAMA\033[m')
print(f'A quantidade de pessoas maiores de 18 anos é {maior18}')
print(f'{homens} homens foram cadastrados.')
print(f'{mulher_menor} mulher(es) possuem menos de 20 anos!')
