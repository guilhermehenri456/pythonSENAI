print('A viagem tem 800 km total')
print('Você ja percorreu 90 km')
print('Há 10 litros no tanque e a cada 7 km gasta 1 litro')
n1 = 800 - 90
n2 = 7 * 10
n3 = n1 - n2
print('Falta percorrer ainda então',n3,' km')
p1 = 640
p2 = 7
c1 = p1 / p2
print('Vai precisar de =',c1, 'litros')
n3 = float(input('Digite o preço da gasola:'))
c2 = c1 * n3
print('O preço total foi:',c2,'reais')