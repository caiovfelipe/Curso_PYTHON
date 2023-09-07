lista_num = []
for numc in range(5):
    num = int(input('Digite um número: '))
    lista_num.append(num)
lista_num.sort()
print(f'O maior número da lista foi o {lista_num[-1]}, e o menor foi o {lista_num[0]}')