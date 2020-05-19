import moeda

p = float(input('Digite um preço: R$ '))
t = int(input('Digite uma taxa em %: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O Dobro de {p} é {moeda.dobro(p)}')
print(f'O aumento  de {p} com taxa de  {moeda.aumentar(p, t)}')
print(f'A diminuição  de {p} com taxa de é {moeda.diminuir(p, t)}')