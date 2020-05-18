from datetime import date
atual = date.today().year
nascimento = int(input('Qual a data de nascimento do atleta: '))
idade = atual - nascimento
print('O atleta com idade de {} anos,'.format(idade))
if idade <= 9:
    print('Esta na categoria Mirim')
elif 9 < idade <= 14:
    print('Esta na categoria Infantil')
elif 14 < idade <= 19:
    print('Esta na categoria Junior')
elif 19< idade <= 25:
    print('Esta na categoria Senior')
else:
    print('Esta na categoria Master')