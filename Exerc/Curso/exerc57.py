import random

nomesf = ['Rafaela', 'Jenifer', 'Claudete', 'Cinderela', 'Aline', 'Maria', 'Adelaine']
nomesm = ['João', 'Cleitinho', 'Carlos', 'Juca', 'Gabriel', 'Afonso', 'Lucas', 'Marinel']
key = random.randint(0,1)
resposta = 0

pessoa = random.choice(nomesm) if key == 1 else random.choice(nomesf)

if key == 1:
    sexo = 'M'
else:
    sexo = 'F'

while resposta != sexo:
    resposta = input('Digite o sexo dessa pessoa {} [M/F]'.format(pessoa)).upper()
    print('Você errou digite novamente!')

print('Parabéns! Agora está correto')
