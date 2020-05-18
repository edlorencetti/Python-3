peso = float(input('Qual o seu peso? (KG): '))
altura = float(input('Qual a sua altura? (m): '))
imc = peso / (altura**2)
print('O seu IMC e : {:.2f}'.format(imc))
if imc <= 18.5:
    print('Vc esta abaixo do peso.')
elif 18.6 < imc <= 25:
    print('vc esta no peso ideal')
elif 25 < imc <= 30:
    print('Vc esta em sobrepeso')
elif 30 < imc <= 40:
    print('Vc esta obeso')
else:
    print('Vc esta com obesidade morbida')
