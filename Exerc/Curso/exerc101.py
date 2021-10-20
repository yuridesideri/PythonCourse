#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18:
        return 'OPCIONAL'
    elif idade >= 18:
        return 'OBRIGATÓRIO'
    else:
        return 'ERRO NO PROGRAMA'

print(voto(2003))






