import random
bot = random.randint(0, 100)  
   

print("")
print("BEM-VINDO AO JOGO DE ADIVINHAÇÃO")
print("")
print("Sou seu computador - Eu estou pensando em um número entre 0 e 100.")
print("Tente adivinhar qual é esse número, Boa Sorte!!")
print("")


   
while True:
    idea = int(input("Digite seu palpite: "))  
    if idea > bot:
        print('O número é menor que', idea)
    elif idea < bot:
        print('O número é maior que', idea)
    elif idea == bot:
        print('Você acertou!')
        print('1 - Para sair')
        print('2 - Para continuar')
        continuar = int(input('Digite sua escolha: '))  
           
        if continuar == 2:
            print("Vamos jogar novamente!")
            bot = random.randint(0, 100)
           
               
        else:
            print("Jogo fechando...")
            break  