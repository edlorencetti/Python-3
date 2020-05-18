nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print('Seu primeiro nome e {} '.format(nome[0]))
print('Seu ultimo nome e {}'.format(nome[len(nome)-1]))
