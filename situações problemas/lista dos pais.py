
import inputs
print("incrições para o evento escolar")
print("")
print("menu de opções")
print("1 - cadastrar um nome")
print("2 - exibir o total de inscritos")
print("3 - exibir a lista de nomes em ordem alfabética")
print("4 - realizar a confirmação de presença dos país")
print("5 - exibir o relatório da chamada")
print("6 - sair")
print("")
presente = []
ausente = []
nomes = []

while True:
    opcao = inputs.input_int("Digite sua escolha")
    if opcao == 1:
        nome = inputs.input_str("digite o nome que quer cadastrar")
        if nome in nomes:
            print("nome cadastrado")
        else:
            nomes.append(nome)
            print("nome cadastrado com sucesso")
    elif opcao == 2:
        print("o total de inscritos foram", len(nomes))
    elif opcao == 3:
        for nome in nomes:
            print(nome)
    elif opcao == 4:
        nome = input("digite um nome para verificar se está presente")
        if nome in nomes:
            presente =inputs.input_str("está presente? sim/não")
            if presented == "sim":
                    presente.append(nome)
                    print("nome adicionado à lista de presentes")
            else:
                ausente.append(nome)
                print("nome adicionado na lista de ausentes")
                print("nome não encontrado")
            
        else:
            ausente.append(nome)
            print("nome adicionado à lista de ausentes")
        
    elif opcao == 5:
        print("lista de presentes:")
        for item in presente:
            print(item)
        print("")
        print("lista de ausentes")
        for item1 in ausente:
            print(item1)
        print("")
        
    elif opcao == 6:
        print("você saiu")
        break
        
    else:
        print("opção inesistente")
                