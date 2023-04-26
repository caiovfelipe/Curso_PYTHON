distancia = float(input('Qual é a distância da sua viagem? '))
if distancia <= 200:
    valor = distancia*0.50
    print('O valor da viagem ficou: R${}'.format(valor))
else:
    valor = distancia*0.45
    print('O valor da viagem ficou: R${}'.format(valor))