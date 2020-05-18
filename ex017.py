from math import hypot
oposto = float(input('qual o valor do cateto oposto:'))
adjacente = float(input('qual o valor do cateto adjacente:'))
'''hipotenusa = ((oposto**2)+(adjacente**2))**(1/2)'''
'''hipotenusa = math.hypot(oposto, adjacente)'''
hipotenusa = hypot(oposto,adjacente)
print('o triangulo retangulo com o cateto oposto {} e cateto adjacente {} tem uma hipotenusa {:.2f}'.format(oposto, adjacente, hipotenusa))