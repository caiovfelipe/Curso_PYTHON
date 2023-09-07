lista_num = []

cnum = int(input('Quantos números deseja contabilizar? '))
for c in range(cnum+1):
    choose = int(input('Digite o número que deseja adicionar: '))
    if choose not in lista_num:
        lista_num.append(choose)
    else:
        print(f'O número {choose} já está na lista')
lista_num.sort()
print(f'Os valores digitados foram: {lista_num}')
