frase = str(input('Digite a frase: '))
pilha = []
for c in frase:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')