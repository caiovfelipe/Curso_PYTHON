def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))


escreva(str(input('Digite uma frase: ')))