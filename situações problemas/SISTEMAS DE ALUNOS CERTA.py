alunos = []
def cadastrar_aluno():
    nome = input("Digite o nome do aluno")
    n1 = float(input("Digite a primeira nota"))
    n2 = float(input("Digite a segunda nota"))
    n3 = float(input("Digite a terceira nota"))
    media = calcular_media(n1,n2,n3)
    verificar = verificar_situacao(media)
    aluno =	{
        "nome": nome,
        "n1": n1,
        "n2": n2,
        "n3": n3,
        "media": media,
        "verificar": verificar,
        }        
    alunos.append(aluno)
    return aluno
def calcular_media(n1,n2,n3):
    return (n1 + n2 + n3) / 3
   
def verificar_situacao(media):
    if media >= 7:
        return "Ficou aprovado"
    elif media < 7 and media >= 5:
        return "Ficou de recuperação"
    elif media < 5:
        return "Ficou reprovado"
def mostrar_relatorio(alunos):
    for arrombados in alunos:
        for chave,valor in arrombados.items():
            print(f"{chave}:{valor}")
        print("")

while True:
    print("SISTEMA DE NOTAS DE ALUNOS")
    print("")
    print("menu de opções")
    print("[1] - cadastrar um nome e as notas")
    print("[2] - mostrar relatório")
    print("[3] - sair")
    print("")
    menu = int(input("Escolha uma opção:  "))
    if menu == 1:
        aluno = cadastrar_aluno()
        print("Você cadastrou todos os dados necessários")        
    elif menu == 2:
        print(mostrar_relatorio(alunos))

    elif menu == 3:
        print("Você saiu!")
        break
    else:
        print("opção inesistente")

