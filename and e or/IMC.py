p = float(input('Digite seu peso em KG ='))
a = float(input('Digite sua altura em metros ='))
m = a * a
IMC = p / m
if IMC <= 18.5:
    print('abaixo do peso')
elif IMC >= 18.5 <= 24.9:
    print('normal')
elif IMC >= 25:
    print('sobrepeso')
elif IMC >= 30:
    print('obesidade')