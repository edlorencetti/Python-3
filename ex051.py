num = int(input('Digite o primeiro termo: ')) # progressao aritmetrica ate o decimo termo
passo =  int(input('Digite o passo: '))
decimo = num + (10 - 1) * passo
for c in range (num, decimo + passo, passo):
    print(' {} '.format(c), end=' - ')
print('ACABOU')