from ex109 import moeda

p = float(input('Digite um preço: R$ '))
t = float(input('Qual a taxa em %?: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O Dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando {moeda.tx(t)}  temos {moeda.aumentar(p, t, True)}')
print(f'Reduzindo {moeda.tx(t)} temos {moeda.diminuir(p, t, True)}')
