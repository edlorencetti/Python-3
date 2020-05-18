celcius = float(input('qual a temperatura em graus celcius:'))
kelvin = celcius + 273.15
farenheit = ((celcius*9)/5)+32
print('a temperatura de {:.2f}graus celcius corresponde a {:.2f} graus farenheit e a {:.2f} graus kelvin'.format(celcius, farenheit, kelvin))
