'''cont = 0
num = 0
soma = 0'''#como soma, cont e num recebem zero podemos colocar tudo em uma linha
num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]'))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um numero [999 para parar]'))
print('vc digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))