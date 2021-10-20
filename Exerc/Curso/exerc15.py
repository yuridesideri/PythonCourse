kmrod = int(input('Insira quantos quilômetros o seu carro rodou: '))
dias = int(input('Digite a quantidade de dias que utilizou o seu carro: '))

precdia = dias * 60 
preckm = kmrod * 0.15
total = precdia + preckm
print('O total a pagar pelos seus usos é R$ {}'.format(total))