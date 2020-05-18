
''' [0] entre colchetes depois do upper seleciona o fatiamento
que sera considerado apeanas a primeira letra e esta letra
sera colocada em maiuscula EX: masculino = M, luiz = L , maior = M, feminino = F'''
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf': #sem necessidade de deixar maiuscula ou minuscula pelo upper
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Seu sexo {} registrado com sucesso'.format(sexo))
