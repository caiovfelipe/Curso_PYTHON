def contador(inicio, fim, passo):
    if passo == 0:
            passo = 1
    if inicio > fim:
            passo *= -1
            fim -= 1
    else:
            fim += 1
    if (inicio > fim):
          fim -= 1
    for c in range(inicio-1, fim, passo):
        
        print(f"{c+1} ", end="")


#De 1 a 10. Depois de -10 a 10. Depois uma jogada personalizada.
print('De 1 a 10, de 1 em 1:')
contador(1, 10, 1)

print('\n De -10 a 10, de 2 em 2:')
contador(-10, 10, 2)

print('\n Agora... uma jogada personalizada.')
contador(int(input('Digite o número de inicio: ')), int(input('Digite número final: ')), int(input('Digite de quanto em quanto: ')))