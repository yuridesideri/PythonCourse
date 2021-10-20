#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.


tuple = ('Abacaxi', 10, 'Lápis', 1.99, 'Chocolate', 5, 'Brinquedo', 20)


for i in range (len((tuple[::2]))):
    print(f'{tuple[2 * i]:.<30} R${tuple[2*i + 1]:.2f}')