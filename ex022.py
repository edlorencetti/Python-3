n = str(input('digite seu nome: ')).strip()
#colocando .strip no final de uma string eliminamos os espacos antes e depois
print('analisando seu nome...')
print('seu nome em maisculas e {}'.format(n.upper()))
print('seu nome em minusculas e {}'.format(n.lower()))
print('seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
print('seu primeiro nome tem {} letras'.format(n.find(' ')))
separa = n.split()
print (separa)
print('seu primeiro nome e {} e ele tem {} letras'.format(separa[0], len(separa[0])))
