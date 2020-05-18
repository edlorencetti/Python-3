from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
computador = randint (0,2)
print('''Suas opcoes: 
[0] pedra
[1] papel
[2] tesoura ''')
jogador = int(input('Qual a sua jogada?: '))
if jogador > 2:
    print('Jogada invalida. Tente novamente')
    exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador ganhou')
    elif jogador == 2:
        print('computador ganhou')

if computador == 1:
    if jogador == 0:
        print('computador ganhou')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador ganhou')

if computador == 2:
    if jogador == 0:
        print('jogador ganhou')
    elif jogador == 1:
        print('computador ganhou')
    elif jogador == 2:
        print('empate')

