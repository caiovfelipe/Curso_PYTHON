'''def area(altura, largura):
    area = altura * largura
    print(f'A aŕea é {area}')
    linha()

def linha():
    print('-'*30)


#Programa
linha()
print('     Calculadora de área')
linha()
area(int(input('Altura: ')), int(input('Largura: ')))
'''

def area(altura, largura):
    resultado = altura * largura
    return int(resultado)


resultado = area(int(input('Altura: ')), int(input('Largura: ')))
print(resultado)