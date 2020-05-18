v = float(input('Qual a velocidade do seu carro em KM/H?'))
if v > 80: #valor maximo da velocidade
    print('MULTADO!! Voce excdeu o limite permitido de 80 KM/H')
    m = (v-80)*7 #valor da multa a partir de 80
    print('Voce deve pagar uma multa de R$ {:.2f}!'.format(m))
print('Tenha um bom dia! Dirija om seguranca!')
