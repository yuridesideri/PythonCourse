#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, 
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show = True):
    for i in range(n, 1, -1):
        if show == True:
            if i != 0:
                print(f'{i} x ', end = '')
            if i == 2:
                print(1)
        n  *= i - 1
    return n





print(fatorial(5))


