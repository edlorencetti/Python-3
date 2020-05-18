'''importante a biblioteca math faz a conversao de radianos entao se faz necessario converter
o angulo em radianos'''
import math
angulo = float(input('digite um angulo em graus:'))
rad = math.radians(angulo)
sen = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)
print(' O angulo de {} graus tem o seno de {:.2f} e o cosseno de {:.2f} e a tangente de {:.2f}'.format(angulo, sen, cos, tang))
