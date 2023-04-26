velocidade = int(input('Digite a velocidade do carro em questão: '))
if velocidade >= 80:
    nv = velocidade - 80
    nvv = nv*7
    print('Ele ultrapassou {}km do limite e terá que pagar R${} de multa'.format(nv, nvv))

#vel = velocidade - 80
#nv = vel*7

