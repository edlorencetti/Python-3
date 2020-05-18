num =(int(input('Digite o primeiro numero: ')),
      int(input('Digite o segundo numero: ')),
      int(input('Digite o terceiro numero: ')),
      int(input('Digite o quarto numero: ')))
print(f'Vc digitou os numeros: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posicao')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print('Os valores pares digitados foram :', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
