# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


import random


tupla = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10), random.randint(0,10))

print(f'Números gerados {tupla}')
print(f'{sorted(tupla)[0]} é o menor número e {sorted(tupla)[-1]} é o maior.')
