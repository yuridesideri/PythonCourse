#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite uma frase qualquer: ')
frasejunta = frase.replace(' ', '')
ainv = frasejunta[::-1].lower().find('a')
qntdletras = len(list(frasejunta))
print('Sua frase possui {} letras "A".'.format(frasejunta.lower().count('a')))
print('A PRIMEIRA letra "A" está na posição {}.'.format(frasejunta.lower().find('a') + 1))
print('A ÚLTIMA letra "A" está na posição {}.'.format(qntdletras - ainv))

