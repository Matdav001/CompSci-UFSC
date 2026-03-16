# Area
# 15 of March of 2026

# Variables declaration
strA, strB, strC = input('Áreas: ').split()

# Variables conversion
A = float(strA)
B = float(strB)
C = float(strC)

# Area calculation
TRIANGULO = (A * C) / 2
CIRCULO = 3.14159 * (C ** 2)
TRAPEZIO = ((A + B) * C) / 2
QUADRADO = B ** 2
RETANGULO = A * B

# Print result
print('TRIANGULO: %.3f' % TRIANGULO)
print('CIRCULO: %.3f' % CIRCULO)
print('TRAPEZIO: %.3f' % TRAPEZIO)
print('QUADRADO: %.3f' % QUADRADO)
print('RETANGULO: %.3f' % RETANGULO)
