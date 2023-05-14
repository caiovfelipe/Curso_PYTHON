import math

num = float(input('Digite um número com vírgula: '))
inte = math.floor(num) #O certo seria TRUNC ou INT
print('O numero inteiro ficaria \033[0;32m{}\033[m.' .format(inte))
