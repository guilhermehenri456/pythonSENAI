anoN = int(input('Digite o ano do nascimento '))
anoA = int(input('Digite o ano atual '))
d = anoA - anoN
if d < 18:
   v = 'maior de idade'
elif d > 18:
    v = 'menor de idade'
print('A pessoa é',v)