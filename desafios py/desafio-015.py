from ast import Num
km = float(input('Quantos km você percorreu?  '))
dias = int(input('Quantos dias você percorreu com o carro?  '))
km_result = km*0.15
dias_result = dias*60
result = km_result + dias_result
print('Você deverá pagar \033[0;31mR${:.2f}\033[m'.format(result))