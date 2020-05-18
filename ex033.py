a = int(input('digite o primeiro valor:'))
b  = int(input('digite o segundo valor:'))
c  = int(input('digite o terceiro valor:'))
# verificando quem e menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# verificando quem e maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado e {}'.format(menor))
print('O maior valor digitado e {}'.format(maior))
