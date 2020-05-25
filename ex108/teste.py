from ex108 import moeda

p = float(input('Digite um preço: R$ '))
print(f'A metade de R$ {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O Dobro de R$ {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%  temos R${moeda.moeda(moeda.aumentar(p, 10))}')
