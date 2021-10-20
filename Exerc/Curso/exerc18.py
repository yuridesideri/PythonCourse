import math
ang = float(input('Escolha um valor de ângulo em graus: '))
rad = math.radians(ang)

seno = math.sin(rad)
cos = math.cos(rad)
tg = math.tan(rad)
print('{:.2f}'.format(seno))
print('{:.2f}'.format(cos))
print('{:.2f}'.format(tg))