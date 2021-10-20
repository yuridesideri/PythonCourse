#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('zero','um','dois', 'três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = input('Digite um número para vê-lo por extenso: ')
    if num.isnumeric() == True:
            if 0 <= int(num) <= 20:
                print(numeros[int(num)])
                break
    print('Um número de [0 a 20]')