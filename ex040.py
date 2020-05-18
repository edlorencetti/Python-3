n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
nota = (n1+n2)/2
if nota >= 7:
    print('Sua nota foi {}.Voce atingiu a media e passou! Parabens.'.format(nota))
elif nota >= 5 and nota <= 6.9: #''' ou if 7 > nota >=5'''
    print('Sua nota foi {}. Voce esta de recuperacao!'.format(nota))
else:
    print('Sua nota foi {}.Voce foi reprovado!!'.format(nota))
