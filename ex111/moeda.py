def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato == False is False else moeda(res)


def diminuir(preço = 0, taxa=0, formato=False ):
    res = preço - (preço * taxa / 100)
    return res if formato == False is False else moeda(res)


def dobro(preço = 0,formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0,formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda} {preço:>.2f}'.replace('.', ',')


def tx (taxa=0, tx='%'):
    return f'{taxa}{tx}'


def resumo(preço=0, taxaa=10, taxar=5):
    print('_' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('_' * 30)
    print(f'Preço analisado:\t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço:\t{metade(preço, True)}')
    print(f'{tx(taxaa)} de aumento:\t{aumentar(preço, taxaa, True)}')
    print(f'{tx(taxar)} de redução:\t{diminuir(preço, taxar, True)}')
    print('_' * 30)