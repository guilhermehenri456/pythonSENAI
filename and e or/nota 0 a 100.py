
n1 = int(input('digite uma nota '))
n2 = int(input('digite outra nota '))
if n1 > 0 and n1 <= 100 and n2 > 0 and n2 <= 100:
    s = n1+n2
    m = s/2
    print('A média foi', m)
    if  m >= 70:
        print('aprovado')
    elif m<= 50:
            print('reprovado')
    elif m < 70 and 50:
            print('recuperação')
else:
    print('Digite uma nota de 0 a 100')



