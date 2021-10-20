import sys
run = True
while run:
    num = input('Coloque um valor: ')
    if num.isnumeric() == True :
        num = int(num)
        print('Muito bem, dado o valor {}, o seu antecessor é {} e o seu sucessor é {}'.format(num, num - 1, num + 1 ))
        sys.exit()
    else:
        print('Um valor numérico por favor!')

