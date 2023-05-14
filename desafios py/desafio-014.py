c = float(input('A temperatura em C°: '))
#f = ((9*c)/5)+32
f = 9*c/5+32
#Não precisamos usar os parenteses por causa da ordem de precedência
print('A temperatura em \033[0;33m{} °C\033[m é \033[0;34m{} °F\033[m '.format(c, f))
