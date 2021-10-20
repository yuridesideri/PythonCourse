#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:     
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada



def contador(i,f,p):
    if i < f:
        print(i)
        for cont in range(f):
            if i + p > f:
                break
            i += p
            print(i)
    elif i > f:
        print(i)
        for cont in range(i):
            if i - p < f:
                break
            i -= p
            print(i)



contador(1,10,1)
contador(10,1,2)





























