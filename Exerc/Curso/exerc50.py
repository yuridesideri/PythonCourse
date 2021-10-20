#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
cont = 0
for i in range(0,6):
    n = int(input('Digite o número {} '.format(i + 1)))
    if n % 2 == 0:
        cont += n
print('O resultado final da soma dos número PARES é {}'.format(cont))