total = mais1000 = menor = cont = 0
nomeml = ''
while True:
    nome = str(input('DIgite o nome do produto: '))
    preco = int(input('Digite o preço do produto: R$'))
    total += preco
    cont += 1
    skipq = ' '
    while skipq not in 'SsNn':
        skipq = str(input('Deseja continuar [S/N]? ')).upper().split()[0]
    if skipq == 'N':
        break

    if preco > 1000:
        mais1000 += 1
    
    if cont == 1 or preco < menor:
        menor = preco
        nomeml = nome



print(f'O total da compra foi de R${total}')
print(f'Foram contabilizados {mais1000} produtos custando mais de R$1000.')
print(f'O produto mais barato foi a(o) {nomeml} custando R${menor}.')