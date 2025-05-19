n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))
if n1 > n2:
    verifica = 'primeiro'
elif n1 < n2:
    verifica = 'segundo'
elif n1 == n2:
    verifica = 'nenhum dos dois pois são iguais'
print('O numero maior é',verifica)