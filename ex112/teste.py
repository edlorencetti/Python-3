from ex112.utilidadecev import moeda
from ex112.utilidadecev import dados

p = dados.leiadinheiro('Digite um preço R$:  ')
ta = dados.leiadinheiro('Qual a taxa de aumento%: ')
tr = dados.leiadinheiro('Qual a taxa de reduçção%: ')
moeda.resumo(p, ta, tr)
