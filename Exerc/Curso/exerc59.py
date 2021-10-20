#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
import sys


key = 4
while key == 4:
    n1 = input('Digite um valor numérico: ')
    n2 = input('Digite outro valor numérico: ')
    if (n1.isnumeric() and n2.isnumeric()) == False:  
        print('Digite valores numéricos apenas')
        sys.exit()
    elif (n1.isnumeric() and n2.isnumeric()) == True:
        n1 = int(n1)
        n2 = int(n2)


    print('-='*20)
    print('MENUZINHO')
    print('-=' * 20)

    key =int(input('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números\n[ 5 ] sair do programa\n Escolha uma ação: '))

    if key == 1:
        soma = n1 + n2 
        print('A soma entre os número \033[34m {} \033[m e \033[34m {} \033[m  é igual a  \033[36m {} \033[m'.format(n1, n2, soma))
        key = 1

    elif key == 2:
        mult = n1 * n2
        print('A multiplicação entre os número \033[34m {} \033[m e \033[34m {} \033[m  é igual a  \033[36m {} \033[m'.format(n1, n2, mult))
        key = 2
        
    elif key == 3:
        ordem = sorted([n1, n2])
        print('O número {} é maior que {}'. format(ordem[-1], ordem[0]))
        key = 3

    elif key == 4:
        print('REINICIANDO')

    elif key == 5:
        print('Programa encerrado')
        sys.exit()
    






