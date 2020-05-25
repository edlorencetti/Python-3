def aumentar(preço=0, taxa=0, formato=False):
    '''
    Função de aumentar o preço e taxa definido por digitação
    :param preço:define o preço a ser aumentado
    :param taxa:a taxa em porcentagem de aumento do preço
    :param formato:formato de reais para o preço
    :return:o preço aumentado na porcentagem inserida em taxa
    '''
    res = preço + (preço * taxa / 100)
    return res if formato == False is False else moeda(res)


def diminuir(preço = 0, taxa=0, formato=False ):
    '''
    Função de reduzir o preço e taxa definido por digitação
    :param preço: preço a ser diminuido
    :param taxa: taxa de diminuição em porcentagem
    :param formato: formato de reais para o preço
    :return: preço diminuido na porcentagem definida na digitação
    '''
    res = preço - (preço * taxa / 100)
    return res if formato == False is False else moeda(res)


def dobro(preço = 0,formato=False):
    """
    Função para dobrar o preço informado na digitação
    :param preço: preço que foi digitado
    :param formato: Formato em reais para o preço digitado
    :return: preço dobrado que foi digitado
    """
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0,formato=False):
    """
    Função para reduzir um preço digitado na metade de seu valor
    :param preço: preço a ser diminuido
    :param formato: formato em reais para o preço digitado
    :return: valor informado na metade do preço informado
    """
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    """
    Função que define a formatação do número digitado como preço
    :param preço: valor digitado como preço
    :param moeda: formatação do preço em reais
    :return: retorna o valor digitado em formato de reais
    """
    return f'{moeda} {preço:>.2f}'.replace('.', ',')


def tx (taxa=0, tx='%'):
    """
    Função para formatar o valor digitado como taxa em %
    :param taxa: valor digitado
    :param tx: texto de % inserido sobre a taxa
    :return: retorna o valor digitado formatado em %
    """
    return f'{taxa}{tx}'


def resumo(preço=0, taxaa=10, taxar=5):
    """
    função que calcula as funções determinadas para o valor digitado
    :param preço: valor digitado
    :param taxaa: valor digitado como taxa de aumento
    :param taxar: valor digitado como taxa de diminuição
    :return: retorna os valores calculados nas funções
    """
    print('_' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('_' * 30)
    print(f'Preço analisado:\t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço:\t{metade(preço, True)}')
    print(f'{tx(taxaa)} de aumento:\t{aumentar(preço, taxaa, True)}')
    print(f'{tx(taxar)} de redução:\t{diminuir(preço, taxar, True)}')
    print('_' * 30)