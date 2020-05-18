from random import randint
computador = randint(0, 10)
print('''Sou seu computador...
Acabei de pense em um numero entre 0 e 10.
Sera que consegue adivinhar qual foi?''')
acertou = False
palpite = 0
while not acertou:
    jogador  = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais....Tente mais uma vez.')
        elif jogador > computador:
            print('Menos....Tente mais uma vez')
print('Acertou!')
print('Vc acertou com {} palpites'.format(palpite))
