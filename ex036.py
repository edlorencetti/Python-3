casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 0.30
print(minimo)
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestacao será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo aprovado')
else:
    print('Emprestimo negado!!')