reta1 = int(input('Digite o tamanho da primeira reta (apenas números): '))
reta2 = int(input('Digite o tamanho da segunta reta (apenas números): '))
reta3 = int(input('Digite o tamanho da terceira reta (apenas números): '))
#Desiguldade triangular => a < b + c
if reta1 >= reta2 + reta3:
    print('Infelizmente você não poderá formar um triangulo com essas 3 retas.')
elif reta2 >= reta1 + reta3:
    print('Infelizmente você não poderá formar um triangulo com essas 3 retas.')
elif reta3 >= reta1 + reta2:
    print('Infelizmente você não poderá formar um triangulo com essas 3 retas.')
else:
    print('Que bom! Você consegue sim formar um triangulo com essas 3 retas!')