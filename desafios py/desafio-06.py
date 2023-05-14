num = int(input('Escolha um numero: '))
num_dobro = num*2
num_triplo = num*3
num_raiz = num**(1/2)
print('Seu dobro é \033[0;32m{}\033[m, seu triplo é \033[0;32m{}\033[m, e sua raiz é \033[0;32m{:.2f}\033[m. '.format(num_dobro, num_triplo, num_raiz))