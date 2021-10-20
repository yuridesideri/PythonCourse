#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaint(a):
    while True:
        num = input(a)
        if num.isnumeric() == False:
            print('Digite um número inteiro válido.')
        
        else:
            return int(num)



def leiafloat(a):
    while True:
        num = input(a)
        try: 
            return float(num)
            
        except ValueError:
            print('Um potencial float por favor')






print(leiaint('Digite seu int: '))

print(leiafloat('Digite seu float: '))



