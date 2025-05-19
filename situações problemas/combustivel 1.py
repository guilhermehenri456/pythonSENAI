#passo passo

#1 - O objetivo é um sistema que calcule o custo para encher o tanque de 50 litros,
#1 - O tanque está com 20 litros de combustivel atualmente e eu preciso completar o tanque onde o litro é 5,80 reais

#2 Calcular a diferença entre 50 litros e 20 litros
#       Para calcular o valor do combustivel entre 20 e 50 litros

#3
#Passo1: Subtrair 50 menos 20 para descobrir quantos litros falta para encher
#passo2: Multiplicar a quantidade de litro por R$ 5,80 o litro
#Passo3: Exibir a o custo final

lt = 50-20
g1 = lt * 5.80
(print('O custo para encher o tanque foi de =',g1, 'reais' ))

n1 = int(input('Digite a quantidade total do tanque'))
n2 = int(input('Digite quanto tem de gasolina no tanque'))
n3 = float(input('Digite o preço da gasolina'))
c1 = n1-n2
c2 = c1 * n3
print('O custo final foi =',c2,'reais')