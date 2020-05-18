from random import randint
v = 0
print('-xx'*10)
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Vc jogou {jogador} e o computador {computador}. Total {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Vc venceu!')
            v += 1
        else:
            print('Vc perdeu!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Vc ganhou!')
            v += 1
        else:
            print('Vc perdeu!!')
            break
print(f'GAME OVER. Vc venceu {v} vezes.')
print('-xx'*10)
