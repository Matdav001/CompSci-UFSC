# BMI calculation
# 16 of March of 2026

# Variables declaration
weight = float(input())
height = float(input())

# BMI calculation
imc = weight / (height ** 2)

# if logic and print result
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')