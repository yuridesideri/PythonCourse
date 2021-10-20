#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.



frase = input('Digite a sua frase: ')
new = frase.lower().replace(' ', '')
if new == new[::-1]:
    print('Parabéns! Encontrastes um PALÍNDROMO!!')
else:
    print('Sua palavra não é um palíndromo!')