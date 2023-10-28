matriz = list()
col1 = list()
col2 = list()
col3 = list()
maior2f = list()
pares = 0

soma3l = 0
for c in range(3):
    num1 = int(input(f'Digite o número para a coordenada (1, {c+1}): '))
    col1.append(num1)
matriz.append(col1[:])
for f in range(3):
    num2 = int(input(f'Digite o número para a coordenada (2, {f+1}): '))
    col2.append(num2)
matriz.append(col2[:])
for d in range(3):
    num3 = int(input(f'Digite o número para a coordenada (3, {d+1}): '))
    soma3l += num3
    col3.append(num3)
matriz.append(col3[:])

for parl in matriz:
    for parn in parl:
        if parn % 2 == 0:
            pares += parn
print("_"*15)
print('Matriz criada com sucesso!')
print('_'*13)
print(f'-', matriz[0][0],'-', matriz[0][1],'-', matriz[0][2], '-')
print('_'*13)
print(f'-', matriz[1][0],'-', matriz[1][1],'-', matriz[1][2], '-')
print('_'*13)
print(f'-', matriz[2][0],'-', matriz[2][1],'-', matriz[2][2], '-')
print('_'*13)
print("_"*15)
print(f'A soma de todos os números pares é equivalente a {pares}')
print(f'A soma dos números da terceira fileira é igual á {soma3l}')
print(f'O maior valor dá segunda fileira é: {max(matriz[1])}')