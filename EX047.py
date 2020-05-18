for cont in range (0,51):
    if cont % 2 == 0:
        print(cont, end= " ")

for cont in range (2,51,2):# este segundo codigo usa menos memoria devido ao passo 2
    print(cont, end=' ')
print('Acabou')