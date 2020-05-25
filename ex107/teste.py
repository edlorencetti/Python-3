from ex107 import moeda

p = float(input('Digite um preço: R$ '))
t = int(input('Digite uma taxa em %: '))
print(f'A metade de R$ {p} é {moeda.metade(p)}')
print(f'O Dobro de R${p} é {moeda.dobro(p)}')
print(f'O aumento  de R${p} com taxa de {t}% é  {moeda.aumentar(p, t)}')
print(f'A diminuição  de R${p} com taxa de {t}% é {moeda.diminuir(p, t)}')