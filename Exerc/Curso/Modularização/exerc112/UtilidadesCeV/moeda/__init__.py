def aumentar(v, p):
    v = v + v*p
    return v

def diminuir(v, p):
    v = v - v*p
    return v

def dobro(v):
    v *= 2
    return v

def metade(v):
    v /= 2
    return v

def moeda(v, key =True):
    if key:
        print(f'Para o valor R${v:.2f}:')
        print(f'O aumento de 10% é R${aumentar(v, 0.1):.2f}')
        print(f'O dobro é R${dobro(v):.2f}')
        print(f'A metade é R${metade(v):.2f}')
