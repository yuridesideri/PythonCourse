#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

cadastro = {}

cadastro["nome"] = input('Digite o nome: ')
nasc = int(input('Digite o ano de nascimento: '))
cadastro["idade"] = 2021 - nasc
cadastro["carteira de trabalho"] = int(input('Carteira de trabalho: (0 se não tem) '))
if cadastro["carteira de trabalho"] != 0:
    ano_cont = int(input('Digite o ano de quando foi contratado: '))
    cadastro["ano de contratação"] = ano_cont
    cadastro["salario"] = float(input('Digite o valor do seu salário: '))
    cadastro["idade de aposentadoria"] = ano_cont + 30 - nasc

for k, v in cadastro.items():
    print(f'O {k} é {v}')
















