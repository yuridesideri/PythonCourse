#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
#nome = input('Digite seu nome completo: ')
#print('Seu nome é: '+ nome)
#print('Seu nome possui "Silva"?')
#print(nome.lower().find('silva') >= 0)

#Refeito o Programa para usa o operador 'in';

nome = input('Digite seu nome completo: ')
print('Seu nome é: '+ nome)
print('Seu nome possui "Silva"?')
print('silva' in nome.lower())

 