metros = float(input('Quantos metros? '))
kilometro = metros / 1000
hectometro = metros / 100
decametro = metros / 10
decimetro = metros * 10
centimetros = metros*100
milimetros = metros*1000
print('Ele tem \033[0;33m{}\033[m kilometros, \033[0;33m{}\033[m hectometros, \033[0;33m{}\033[0;33m decametros, \033[0;33m{}\033[m decimetros, \033[0;33m{}\033[m centimetros e \033[0;33m{}\033[m milimetros.'.format(kilometro, hectometro, decametro, decimetro, centimetros, milimetros))