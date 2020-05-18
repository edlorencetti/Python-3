n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digito o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opcao = int(input('Qual e a sua opcao?'))
    if opcao == 1:
        print('A soma entre {} e {} e {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('O produto entre {} e {} e {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, {} e maior'. format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digito o segundo valor: '))
    else:
        print('Opcao invalida. Tente novamente.')
    print( '=-=' * 10)
print('Fim do programa! Volte sempre!')
