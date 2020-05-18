from random import choice
n1 = input('nome do aluno 1:')
n2 = input('nome do aluno 2:')
n3 = input('nome do aluno 3:')
n4 = input('nome do aluno 4:')
lista = [n1, n2, n3, n4]
#importanto o metodo choice da biblioteca random nao ha necessidade de colocar a biblioteca ex:random.choice
escolhido = choice(lista)
print('O escolhido e:{}'.format(escolhido))
