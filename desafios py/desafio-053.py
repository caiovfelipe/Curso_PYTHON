f = str(input('Digite a frase para verificar se ela é um palindromo: ')).strip()
p = f.split()
j = ''.join(p)
i = j[::-1]
print('O inverso da palavra {} é {}'.format(p, i))
if i == j:
    print('Temos um palíndromo!')
else:
    print('A frase ditada não é um palíndromo.')