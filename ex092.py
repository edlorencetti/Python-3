from datetime import datetime
dados =  dict()
dados['nome'] = str(input('nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano da contratacao: '))
    dados['Salario'] = float(input('Salario: R$ '))
    dados['Aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'  -{k} tem o valor {v}')
