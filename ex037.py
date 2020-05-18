num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal''')
opcao = int(input('Sua opcao: '))
if opcao == 1 :
    print('{} convertido para binario {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal {}'.format(num, hex(num)[2:]))
else:
    print('Numero invalido, tente outra vez.')