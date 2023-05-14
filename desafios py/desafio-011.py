largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
area = largura*altura
tinta = area / 2
print('Sua parede tem uma área de \033[0;34m{}m²\033[m, e para pintar está parede você precisara de \033[0;31m{}L\033[m de tinta.'.format(area, tinta))