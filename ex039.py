from datetime import date
atual = date.today().year
n = int(input('Qual o ano do seu nascimento?: '))
idade = atual - n
alistamento = n + 18
print('Quem nasceu em {} tem {} anos em {}'.format(n, idade, atual))
if idade == 18:
    print('Voce tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Voce nao tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
else:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado ha {} anos'.format(saldo))
    ano =  atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
