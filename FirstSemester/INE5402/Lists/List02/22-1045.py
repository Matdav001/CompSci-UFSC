# Triangles types
# 18 of March of 2026

# Variables declaration
a, b, c = input('Dimensões do triângulo: ').split()

at = float(a)
bt = float(b)
ct = float(c)

# Sort decrescent
if ct > at and ct > bt:
    a = ct
    if at > bt:
        b = at
        c = bt
    else:
        c = at
        b = bt
elif bt > at and bt > ct:
    a = bt
    if at > ct:
        b = at
        c = ct
    else:
        c = at
        b = ct
else:
    a = at
    if bt > ct:
        b = bt
        c = ct
    else:
        c = bt
        b = bt



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
