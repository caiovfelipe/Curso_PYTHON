cont = soma = 0
while True:
    n = int(input('Digite um número [999 para parar a execução.]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram contabilizados {cont} números e a soma deles foi um total de {soma}.')
print('Execução encerrada.')