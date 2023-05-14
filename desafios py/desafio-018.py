from math import radians, sin, cos, tan

an = float(input('Digite o angulo que você deseja: '))
cosseno = cos(radians(an)) #Descobre o cosseno
tangente = tan(radians(an)) #Descobre a tangente
seno = sin(radians(an)) #Descobre o seno
print('O ângulo de {} tem o seno de \033[0;32m{:.2f}\033[m' .format(an, seno))
print('O angulo de {} tem o cosseno de \033[0;32m{:.2f}\033[m' .format(an, cosseno))
print('O angulo de {} tem a tangente de \033[0;32m{:.2f}\033[m' .format(an, tangente))