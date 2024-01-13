'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a+b
    print(f'A soma de A + B = {s}')



soma(4, 5)
soma(8, 9)
soma(2, 1)'''


'''
def contador(*num):
    print(num)



contador(2, 1, 7)
contador(9, 0)
contador(3, 5, 6, 2, 4, 6)

#cria uma tupla'''



def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)




'''
a = 4
b = 5
s = a+b
print(s)
a = 9
b = 8
s = a+b
print(s)
a = 2
b = 1
s = a+b
print(s)'''