print('{:=^40}'.format(' Lojas Guanabara ')) # informação centralizada em 40 espaços entre sinais de igual
preco = float(input('Preço das suas compra: R$ '))
print(''' Formas de pagamento:
[1] à vista no dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão ''')
opcao =  int(input('Qual a opcao?: '))
if opcao == 1:
    total = preco * 0.90
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('Sua compra sera parcelada em duas parcelas de R$ {:.2f}'. format(parcela))
elif opcao == 4:
    total = preco * 1.2
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {} parcelas de R$ {:.2f}'.format(totparc, parcela))
else:
    total = preco
    print('Opcao de compra errada. Tente outra vez!!')
print('A sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(preco, total))
