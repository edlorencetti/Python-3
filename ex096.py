def area(l, c):
    a = l * c
    print(f'A area de um terreno {l}x{c} e de {a}m2. ')


print('    Controle de terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)