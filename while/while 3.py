quanti = 0
valor_total = 0

while True :
    print("[0] sair")
    print("[1] adicionar o valor da despesa")
    print("[2] mostrar a quantidade e o valor total das depesas")

    opcao = int(input("escolha uma opção: "))

    if opcao == 1:
        #add_despesa()
        d = float(input("adicione o valor da despesa: "))
        quanti = quanti + 1
        valor_total = valor_total + d
        print("O valor da depesa é =",d)
   
    elif opcao == 2 :
        #quanti_valor ()
        print("A quantidade de despesa é ",quanti,"e o valor delas é ",valor_total)
   
    elif opcao == 0 :
        print("você saiu")
        break
