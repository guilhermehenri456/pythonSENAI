#é a 3 da situação problema
def  subtração(n1, n2):
    return n1 - n2

def adição(n1, n2):
    return n1 + n2

def multiplicação(n1, n2):
    return n1 * n2

def divisão(n1, n2):
    return  n1 / n2

def mostrar_contas(n1, n2):
    print("a conta usando subtração é",subtração(n1,n2))
    print("a conta usando adição é",adição(n1,n2))
    print("a conta usando multiplicação é",multiplicação(n1,n2))
    print("a conta usando divisão é",divisão(n1,n2))
    
n1 = float(input("Digite um número"))        
n2 = float(input("Digite um número"))
    
mostrar_contas(n1, n2)

#é a 3.1 da situação problema
def subtração (n1, n2):
    return n1 - n2
   
def adição (n1, n2):
    return n1 + n2

def multiplicação(n1, n2):
    return n1 * n2
   
def divisão (n1, n2):
    return n1 / n2

def mostrar_operacao(n1, n2):
    print("subtração =",subtração(n1,n2))
    print("adição =",adição(n1,n2))
    print("multiplicação =",multiplicação(n1,n2))
    print("divisão =",divisão(n1, n2))



n1 = float(input("Digite um número ="))        
n2 = float(input("Digite um número ="))

mostrar_operacao(n1, n2)
#é a 3.2 da situação problema
def menu_calculadora():
    print("Menu:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("5 - Todas as opções")

def soma(n1, n2):
    return n1 + n2

def subtração(n1, n2):
    return n1 - n2

def divisão(n1, n2):
    return n1 / n2

def multiplicação(n1, n2):
    return n1 * n2

def conta_escolhida():
    if conta == 1:
        print("O resultado da soma é", soma(n1, n2))
    elif conta == 2:
        print("O resultado da subtração é", subtração(n1, n2))
    elif conta == 3:
        print("O resultado da divisão é", divisão(n1, n2))
    elif conta == 4:
        print("O resultado da multiplicação é", multiplicação(n1, n2))
    else:
        print("O resultado da soma é", soma(n1, n2))
        print("O resultado da subtração é", subtração(n1, n2))
        print("O resultado da divisão é", divisão(n1, n2))
        print("O resultado da multiplicação é", multiplicação(n1, n2))

n1 = int(input("Escolha um número: "))
n2 = int(input("Escolha outro número: "))

menu_calculadora()
conta = int(input("Escolha uma opção: "))

conta_escolhida()


