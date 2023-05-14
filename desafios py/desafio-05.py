num = int(input('Escolha um numero: '))
num_ants = num - 1
num_dps = num + 1
print('O seu antessesor é \033[0;32m{}\033[m e seu sucessor é \033[0;32m{}\033[m'.format(num_ants, num_dps))