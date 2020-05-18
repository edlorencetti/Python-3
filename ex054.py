from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range (0,7):
    nasc = int(input('Digite o ano que a pessoa {} nasceu pessoa: '.format(c+1)))
    idade = atual - nasc
    if idade >=21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de 21'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de 21'.format(totmenor))
