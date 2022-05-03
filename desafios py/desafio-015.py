from ast import Num


km = float(input('Quantos km você percorreu?  '))
dias = int(input('Quantos dias você percorreu com o carro?  '))
km_result = km*0.15
dias_result = dias*60
result = km_result + dias_result
input('Você deverá pagar R${:.2f}'.format(result))