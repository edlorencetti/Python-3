#calcular a porcentagem de aumento de um funcionario perguntando seu aumento e salario atual
atual = float(input('qual o salario atual do funcionario? R$:'))
aumento = float(input('qual a porcentagem de aumento para o funcionario? em %='))
porcentagem = (aumento/100)+1
ajuste = porcentagem*atual
print('o salario atual de R${:.2f} com aumento de {:.0f}%, o novo salario sera de R${:.2f}'.format(atual, aumento, ajuste))
