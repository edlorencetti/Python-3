from ex111.utilidadecev import moeda
from ex111.utilidadecev import dados

p = float(input('Digite um preço R$:  '))
ta = float(input(' Qual a taxa de aumento%: '))
tr = float(input('Qual a taxa de reduçção%: '))
moeda.resumo(p, ta, tr)
