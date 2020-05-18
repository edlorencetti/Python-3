total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco: R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
        ''' podemos simplificar os doi blocos de preco mais barato eliminando o else e colocando na primeira lina com o contador
        if cont == 1 or preco < menor:
            menor = preco
            barato = produto'''
    resp = ' '
    while resp not in 'SN':
        resp =  str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1.000,00')
print(f'O menor preco foi o produto {barato} de R$ {menor:.2f}')
