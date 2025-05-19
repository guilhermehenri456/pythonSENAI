#passo passo

#1 - Exibir o novo salario e o aumento

#2 - Descobrir 10% do salario

#3 - Resultado da conta

#Passo1: Multiplicar o salario atual pela porcentagem
#Passo2: Divida o salario depois do da porcentagem por 100
#Passo3: Exibir o aumento do salario depois e de quanto foi esse aumento

salario = float(input('Digite um salario'))
aumento = salario * 10
aumento_salario = aumento / 100
print('O seu aumento salarial de acordo com a porcentagem foi', salario + aumento_salario, ' reais')
print('O seu salario aumentou', aumento_salario, ' reais')
