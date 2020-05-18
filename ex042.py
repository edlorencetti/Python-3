r1 = float(input('Primeiro segimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    if r1 == r2 == r3:
        print('Os seguimentos podem formar um triangulo EQUILATERO')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Os seguimentos formam um triangulo ISOSCELES')
    else:
        print('Os seguimentos formam um triangulo ESCALENO')
else:
    print('Os seguimento nao podem formar um triangulo')
