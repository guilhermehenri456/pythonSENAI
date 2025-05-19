from  datetime import datetime

def hora_função(nome):  
    hora_dia = datetime.now().hour

    if hora_dia >= 0 and hora_dia <= 5:
        print("Boa madrugada", nome)
    elif hora_dia >= 5.1 and hora_dia <= 12:
        print("Bom Dia", nome)
    elif hora_dia >= 12.1 and hora_dia <= 19:
        print("Boa Tarde", nome)
    elif hora_dia >= 19.1 and hora_dia <= 23.59:
        print("Boa Noite", nome)
        
nome = input("Digite seu nome: ")
hora_função(nome)



