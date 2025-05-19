nota = int(input('digite uma nota '))
nota2 = int(input('Digite outra nota '))
m = nota + nota2
n = m / 2

if n < 70:
    verifica = 'reprovado'
elif n >= 70:
    verifica = 'aprovado'
print('O aluno foi',verifica)