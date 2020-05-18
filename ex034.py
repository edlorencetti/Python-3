salario = float(input('Qual o valor do seu salario R$?'))
if salario < 1250:
    print ('Seu salario com reajuste e de R$ {:.2f}'.format(salario*1.15))
else:
    print('Seu salario com reajuste e de R$ {:.2f}'.format(salario*1.10))
