#é a 3 da situação problema
import inputs
def mostrar_contas(n1, n2):
    print("a conta usando subtração é",subtração(n1,n2))
    print("a conta usando adição é",adição(n1,n2))
    print("a conta usando multiplicação é",multiplicação(n1,n2))
    print("a conta usando divisão é",divisão(n1,n2))
    
def  subtração(n1, n2):
    return n1 - n2
def adição(n1, n2):
    return n1 + n2
def multiplicação(n1, n2):
    return n1 * n2
def divisão(n1, n2):
    return  n1 / n2



def menu(n1,n2):
    while True:
        try:
            print("1 - subtração")
            print("2 - adição")
            print("3 - multiplicação")
            print("4 - divisão")
            print("5 - exibir todas")
            
            n = inputs.input_int("Digite de 1 a 5")
            
            if n == 1:
                print(subtração(n1,n2))
            elif n == 2:
                print(adição(n1,n2))
            elif n == 3:
                print(multiplicação(n1,n2))
            elif n == 4:
                print(divisão(n1,n2))
            elif n == 5:
                mostrar_contas(n1,n2)
            else:
                print("Digite um número valido por favor")
        except ValueError:
            print("Digite um número de 1 a 5")
            
            
while True:
        n1 = inputs.input_float("Digite apenas números")
        n2 = inputs.input_float("Digite apenas números")
        break




menu(n1, n2)