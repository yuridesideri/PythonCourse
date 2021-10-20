
class Matematica:
    def __init__(self):
        Num1 =(input('Digite o primeiro número: '))
        if Num1.isnumeric() != True:
            print('Digita um NÚMERO!')
            quit()
        if Num1.isnumeric() == True: 
            Num1 = int(Num1)  

        Num2 = (input('Digite o segundo número: '))
        if Num2.isnumeric() != True:
            print('Digita um NÚMERO! ')
            quit()
        if Num2.isnumeric() != False:
            Num2 = int(Num2)

        soma = int(input('Qual a soma dos valores? '))
        Num3 = Num1 + Num2
        if Num3 != soma:
            soma = None
        print(bool(soma))
    

Matematica()