nome = input('Digite seu nome completo: ')
#Tudo em maiúscula:
maiuscula = nome.upper()
print('Seu nome em letras maiúsculas é {}'.format(maiuscula))
#Tudo em minúscula:
minuscula = nome.lower()
print('Seu nome em letras minúsculas é {}'.format(minuscula))
#Quantidade de letras sem espaços:
junto = nome.replace(' ', '')
qntdletras = len(junto[:])
print('O seu nome possui {} letras'.format(qntdletras))
#Quantidade de letras do primeiro nome:
separado = nome.split()
primeironome = separado[0]
qntdprimeironome = len(primeironome)
print('A quantidade de letras do seu primeiro nome é {}'.format(qntdprimeironome))