dim1 = int(input('Coloque a largura da sua parede "em metros" '))
dim2 = int(input('Coloque agora a altura da sua parede "em metros" '))
area = dim1 * dim2
tinta = area / 2
print('A área da sua parede é {}.'.format(area))
print('Você vai precisar de {} litros de tinta' .format(tinta))