n = int(input('digite um numero: '))
#utilizando um metodo transformando em string, mas falha nao utilizando milhar
'''n1 = str(n)
print('analisando o numero: {}'.format(n))
print('A unidade e {}'.format(n1[3]))
print('A centena e {}'.format(n1[2]))
print('A dezena e {}'.format(n1[1]))
print('O milhar e {}'.format(n1[0]))'''
#utilizando metodo matematico utilizando divisao inteira e resto
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('A unidade e {}'.format(u))
print('A centena e {}'.format(d))
print('A dezena e {}'.format(c))
print('O milhar e {}'.format(m))
