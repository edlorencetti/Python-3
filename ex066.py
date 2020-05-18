cont = soma = 0
while True:
    num = int(input('Digite um numero [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Vc digitou {cont} numeros e a soma foi {soma}')