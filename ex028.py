from random import randint
from time import sleep
#sleep deixa um tempo ate o algoritmo continuar
computador = randint (0 , 5) # faz o computador pensar
print("-=-"*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('em que numero eu pensei? '))#jogador tenta adivinhar o numero
print('Processando...')
sleep (2)
if jogador == computador:
    print('Parabens vc conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e vc no numero {}!'.format(computador, jogador))
