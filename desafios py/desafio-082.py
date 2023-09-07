list1 = []
listapar = []
listaimp = []
quant = int(input('Quantos números deseja adicionar? '))
for c in range(quant):
    choose = int(input('Digite um número: '))
    list1.append(choose)
for i in list1:
    if i%2 == 0:
        listapar.append(i)
    else:
        listaimp.append(i)
print(f'A lista contabilizada é a seguinte: {list1}')
print(f'Os números pares contabilizados foram: {listapar}')
print(f'Os números ímpares contabilizados foram: {listaimp}')