def calcular_frete (peso1, distancia1):
    peso2 = peso1 * 0.5
    distancia2 = distancia1 * 0.1
    taxa = 10
    valor = peso2 + distancia2 + taxa
    print("O valor do frete foi ", valor)
    

peso1 = int(input("Digite um peso aleátorio"))
distancia1 = int(input("Digite uma distância aleátoria"))
calcular_frete(peso1, distancia1)