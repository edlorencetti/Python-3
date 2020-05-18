num = int(input('Digite um numero: ')) # numero par e impar
resultado = num % 2
if resultado == 0:
    print('\033[034m  O numero {} e par'.format(num))
else:
    print('\033[35m O numero {} e impar'.format(num))