import math
cat_a = float(input('Digite o cateto adjecente: '))
cat_o = float(input('Digite o cateto oposto: '))
hipt = math.sqrt(cat_a * cat_a + cat_o * cat_o) #--> HYPOT seia o ideal
print('A hipotenusa do triângulo retângulo que deseja descobrir é \033[0;32m{:.2f}\033[m'.format(hipt))   

'''co = float(input('Comprimento do cateto oposto: '))
ca = float('Coprimento do cateto adjacente: ')'''