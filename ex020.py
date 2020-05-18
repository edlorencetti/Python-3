import random
n1 = input('nome do aluno 1:')
n2 = input('nome do aluno 2:')
n3 = input('nome do aluno 3:')
n4 = input('nome do aluno 4:')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('a sequencia escolhida foi:')
print(lista)
