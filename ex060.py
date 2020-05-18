'''from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
print(' O fatorial de {} e {}.'.format(n, f))'''

n = int(input('Digite um numreo para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end=" ")
    print('x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
