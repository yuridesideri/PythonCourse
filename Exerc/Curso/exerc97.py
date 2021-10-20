#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 


def escreva(str):
    tam = (len(str) + 4)
    print('=' * tam)
    print(f'  {str}')
    print('=' * tam)


escreva('Hello World')















