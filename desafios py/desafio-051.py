a1 = int(input('Digite o termo inicial da progressão aritmédica: '))
r = int(input('Digite a razão: '))
n = int(input('Quantos elementos deseja exibir?: '))
l = a1 + (n-1)*r
l += 1
for result in range(a1, l, r):
    print(result)