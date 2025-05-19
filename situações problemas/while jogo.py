import random
print("Bem Vindo ao nosso jogo somos levelUp")
print("O jogo se trata de impar ou par, uma brincadeira da infância agora como jogo! ")
nome = input("Digite seu nome jogador = ")


while True :
    print("Escolha o que você quer")
    print("[0] sair")
    print("[1] Par")
    print("[2] Impar")
    opcao = int(input("escolha uma opção: "))
    if opcao == 0:
        print("Você saiu")
        break
    n1 = int(input("Digite seu número de 0 a 10 = "))
    n2 = random.randint(0,10)
    total = n1 + n2
    print("")
    print("O bot escolheu o número",n2)
    print("Você escolheu o número",n1)
    print("")

    if opcao == 1 and total % 2 == 0:
        print("O resultado é ", total, ", número par, você ganhou!")
    elif opcao == 1 and total % 2 == 1:
        print("O resultado é ", total, ", número impar, você perdeu!")
    elif opcao == 2 and total % 2 == 0:
        print("O resultado é ", total, ", número par, você perdeu!")
    elif opcao == 2 and total % 2 == 1:
        print("O resultado é ", total, ", número impar, você ganhou!")
    
    
  
            
            
        
        
    


        

    




