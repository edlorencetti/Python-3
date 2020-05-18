print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = 0
n2 = 1
termo = int(input('Quantos termos vc quer mostrar? '))
print('{} - {}'.format(n, n2), end='')
cont = 3
while cont <= termo:
    n3 = n + n2
    print(' - {}'.format(n3), end='')
    n = n2
    n2 = n3
    cont += 1
print(' - FIM')
