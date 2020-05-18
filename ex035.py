print('-=-'*20)
print('            Vamos analisar um triangulo?')
print('-=-'*20)
r1 = float(input('Digite um seguimento de reta: '))
r2 = float(input('Digite outro seguimento de reta:'))
r3 = float(input('Digite o terceiro seguimento de reta:'))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print(' Os tres seguimentos {}, {}, {} formam um triangulo'.format(r1, r2,r3))
else:
    print('Os seguimentos {}, {}, {} nao podem formar um triangulo'.format(r1, r2, r3))
