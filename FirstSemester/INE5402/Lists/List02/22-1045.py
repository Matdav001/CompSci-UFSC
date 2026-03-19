# Triangles types
# 18 of March of 2026

# Variables declaration
a, b, c = input('Dimensões do triângulo: ').split()

# Variable conversion
a, b, c = float(a), float(b), float(c)

# Sort decrescent
if a >= b and a >= c:
    a, b, c = a, b, c
elif b >= a and b >= c:
    a, b, c = b, a, c
else:
    a, b, c = c, a, b

if b < c:
    b, c = c, b


# If logic and print result
if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif a**2 == (b**2) + (c**2):
    print('TRIANGULO RETANGULO')
elif a**2 > (b**2) + (c**2):
    print('TRIANGULO OBTUSANGULO')
elif a**2 < (b**2) + (c**2):
    print('TRIANGULO ACUTANGULO')
if a == b == c:
    print('TRIANGULO EQUILATERO')
elif a == b != c or c == a != b or b == c != a:
    print('TRIANGULO ISOSCELES')
