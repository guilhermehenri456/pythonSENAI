futebol1 = {
    "time": "corinthians",
    "paulistas": 30,
    "melhor": True
}

futebol2 = {
    "time": "santos",
    "paulistas": 22,
    "melhor": False
}

futebol3 = {
    "time": "palmeiras",
    "paulistas": 28,
    "melhor": False 
}


#Exibir uma lista de Dicionários
lista_futebol = [futebol1, futebol2,futebol3]

    # Escolhendo os campos
for futebol in lista_futebol:
    print(f"{futebol['time']}")
    print(f"{futebol['paulistas']}")
    print(f"{futebol['melhor']}")
    
for futebol in lista_futebol:
    for chave, valor in futebol.items():
        print(f"{chave} - {valor}")
    print()

# Exibindo todos