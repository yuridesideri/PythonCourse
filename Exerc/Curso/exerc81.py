#Crie um programa que vai ler vários números e colocar em uma lista.                 
#  Depois disso, mostre:                                                                                                                                              
#   A) Quantos números foram digitados.                                                                                                                   
#  B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.

está = 'Não'
lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    key = input('Deseja continuar? [S/N] ')
    if key in 'Nn':
        break
    if num == 5:
        está = 'Sim'

print(f'Foram digitados {len(lista)} números.')
print(f'A lista em ordem descrescente é {sorted(lista)[::-1]}')
print(f'O valor 5 {está} está na lista')
