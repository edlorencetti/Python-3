print('GERADOR DE PA')
print('-=' *10)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razao:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos vc quer mostrar a mais?' ))
print('Progressao com {} termos mostrados'.format(total))
print('FIM')
