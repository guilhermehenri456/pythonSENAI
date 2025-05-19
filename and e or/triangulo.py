print('Digite o tamanho dos lados do triângulo')
l1 = input('Digite o primeiro lado = ')
l2 = input('Digite o segundo lado = ')
l3 = input('Digite o terceiro lado = ')
if l1 == l2 and l2 == l3:
    print('O triângulo é equilátero')
elif l1 != l2 and l1 ==l3:
    print('O triangulo é isósceles')
elif l2 != l1 and l2 ==l3:
    print('O triângulo é isósceles')
elif l3 != l1 and l3 ==l2:
    print('O triângulo é isósceles')
elif l1 != l2 and l1 != l3 and l2 != l1 and l2 != l3 and l3 != l1 and l3 != l2:
    print('O triângulo é escaleno')

    
   