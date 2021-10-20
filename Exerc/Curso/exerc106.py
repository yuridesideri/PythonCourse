# Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
# Importante: use cores.

while True:

    func = input('Digite a função que deseja olhar:')
    print(f'\033[42m{str(help(func))}\033[m')

    if func == 'FIM':
        break























