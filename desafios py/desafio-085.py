todos = list()
par = list()
impar = list()
max = min = 0
while True:
    num = int(input('Digite um número: '))
    if num % 2 == 1:
        impar.append(num)
    else:
        par.append(num)
    resp = str(input('Deseja continuar? (S/N) '))
    if resp in "Nn":
        todos.append(par[:])
        todos.append(impar[:])
        todos.sort()
        break
print(f'Os números pares digitados foram: {par}')
print(f'Os números ímpares digitados foram: {impar}')

