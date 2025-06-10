
def verificar_posi_nega(numero):
    if numero >= 0:
       return True
    
    elif numero < 0:
        return False 
               
numero = int(input("Digite um número"))

verificar_posi_nega(numero)