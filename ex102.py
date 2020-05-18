def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número informado.
    :param n: O número a ser calculado.
    :param show: Mostra ou não a conta do fatorial.
    :return:Valor fatorial do número solicitado.
        """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


help(fatorial)
num = int(input('Insira um número: '))
print(fatorial(num, show=True))