#passo passo

#1 - novo preço do produto
#     quanto diminui

#2 - nome do produto e o preço
#   um desconto de 5%
#   novo preço
#   quanto o valor do produto diminui

#3 -
#Passo1 qual o nome do produto
#Passo2 o valor do produto
#Passo3 adicionar o cupom de desconto
#Passo4 exibir o valor do produto com desconto
#Passo5 subtrair o valor desconto pelo preço


input('Digite o nome do produto')
produto = float(input('Qual o preço do produto?'))
preço =  produto * 5
preço_final = preço / 100
print('O preço final do produto foi de', produto - preço_final, ' reais')
print('O desconto do produto foi', preço_final, ' reais')
