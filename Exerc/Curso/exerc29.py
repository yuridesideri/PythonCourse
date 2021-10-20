#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
import random

vel = random.randint(20, 180)
print('A velocidade escolhida é {} km/h'.format(vel))
if vel <= 80:
    print('Relaxa amigo, sem multas para você!')
else: 
    exc = vel-80
    price = exc * 7
    print('Você ultrapassou o limite de 80km/h. Aqui está uma multa de R$ {}'.format(price))
