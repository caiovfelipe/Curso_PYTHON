largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
area = largura*altura
tinta = area / 2
print('Sua parede tem uma área de {}m², e para pintar está parede você precisara de {}L de tinta.'.format(area, tinta))