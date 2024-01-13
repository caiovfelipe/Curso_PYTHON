def maior(* num):
    cont = maior = 0
    for valor in num:
        print(valor, end=' ', flush=True)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    '''if len(num) >= 1:
        print(f'O maior valor foi {max(num)}.')
    else:
        print('O maior valor foi 0.')'''
    print(f'\nO maior número contabilizado foi: {maior}')



maior(1, 8, 6, 2, 9)
maior(1, 5, 0, 4)
maior(7, 3, 8)
maior(5, 9)
maior(6)
maior()


