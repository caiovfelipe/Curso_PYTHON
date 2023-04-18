name = str(input('Escreva uma frase de sua preferencia: ')).strip().lower()
count1 = name.find('a')
count2 = name.rfind('a')
print('A letra A apareceu no seu texto pela primeira vez na posição {} e pela ultima vez na posição {}'.format(count1, count2))

