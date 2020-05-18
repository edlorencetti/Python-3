dia = int(input('quantos dias o carro foi alugado?'))
km = float(input('quantos kilometros foram rodados nesses dias'))
total = (dia*60)+(km*0.15)
print('com {} dias alugados e rodando {} km, o total gasto de aluguel do carro sera de R${:.2f}'.format(dia, km, total))
