# BMI calculation
# 16 of March of 2026

# Variables declaration
WEIGHT = float(input())
HEIGHT = float(input())

# BMI calculation
IMC = WEIGHT / (HEIGHT ** 2)

# If logic and print result
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC < 25:
    print('Peso ideal')
elif IMC < 30:
    print('Sobrepeso')
elif IMC < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')