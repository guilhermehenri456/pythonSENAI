def tempo():
    temp_hora = (km / velocidade) * 100
    temp_dia = temp_hora / 24
    print("Em horas deu",temp_hora ,"- Em dia deu", temp_dia)

km = float(input("Digite uma distância"))
velocidade = float(input("Digite uma velocidade"))
tempo()