lista = []
numc = 0
quant = int(input('Digite a quantidade de números que deseja colocar na lista: '))
for c in range(quant):
    num = int(input('Digite um número: '))
    lista.append(num)
    numc += 1
lista.sort(reverse=True)
print(f'Foram digitados {numc} números.')
print(f'A lista em forma decescente é a seguinte: {lista}')
if 5 in lista:
    print('O número 5 aparece na lista.')
else:
    print('O número 5 não aparece na lista.')