def input_int(mensagem):
    while True:
        try:
            nome = int(input(mensagem))
            return nome
        except ValueError:
            print("Digite apenas números")
            
def input_float(mensagem,decimal = 2):
    while True:
        try:
            nome = float(input(mensagem))
            return round(nome, decimal)
        except ValueError:
            print("Digite apenas números")
            
def input_str(mensagem):
    while True:
        nome = str(input(mensagem))
        if not nome.isalpha():
            print("Digite apenas números")
        else:
            return nome 
        
        
