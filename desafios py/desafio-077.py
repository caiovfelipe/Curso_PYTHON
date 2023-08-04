palavras = ()
resp = 'S'
while resp not in 'Nn':
    palavra = str(input('Digite uma palavra: '))
    palavras += (palavra, )
    resp = str(input('Deseja continuar? [S/N]: '))
for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')