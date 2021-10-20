#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite seu nome completo: ')
print('Seu primeiro nome é {}, e seu sobrenome é {}. Correto?'.format(nome.split()[0], nome.split()[-1]))
