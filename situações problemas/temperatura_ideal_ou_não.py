def verificar_temp(estacao,temperatura,umidade):
    if estacao == "verão":
        if temperatura >= 23 and temperatura <= 26:
            if umidade >= 40 and umidade <= 65:
                print("A qualidade do ar verão está boa no verão")
        else:
            print("A qualidade do ar no verão é ruim")
    elif estacao == "inverno":
        if temperatura >= 20 and temperatura <= 22:
            if umidade >= 40 and temperatura <= 55:
                print("A qualidade do ar no inverno está boa")
        else:
            print("A qualidade do ar no inverno está ruim")
while 1:
    try:
        estacao = input("Digite uma estação do ano")
        if estacao == "verão" and estacao == "inverno":
            break
    except ValueError:
        print("Coloque uma estação entre verão e inverno")
while 1:
    try:
        temperatura = float(input("Digite a temperatura atual"))
        break
    except ValueError:
        print("Coloque somente números valídos")
while 1:   
    try:
        umidade = float(input("Digite a umidade atual"))
        break
    except ValueError:
        print("Digite somente números válidos")
        

print(verificar_temp(estacao,temperatura,umidade))