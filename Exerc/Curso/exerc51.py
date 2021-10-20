#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

n = int(input('Digite o Primeiro Termo da P.A. '))
q = int(input('Digite a razão da P.A. '))

print('O primeiro termo é', n)
for i in range(n, n + 9):
    n += q
    print(n)