# Area
# 15 of March of 2026

# Variables declaration
a, b, c = input('Áreas: ').split()

# Variables conversion
a, b, c = float(a), float(b), float(c)

# Area calculation
triangulo = (a * c) / 2
circulo = 3.14159 * (c ** 2)
trapezio = ((a + b) * c) / 2
quadrado = b ** 2
retangulo = a * b

# Print result
print('TRIANGULO: %.3f' % triangulo)
print('CIRCULO: %.3f' % circulo)
print('TRAPEZIO: %.3f' % trapezio)
print('QUADRADO: %.3f' % quadrado)
print('RETANGULO: %.3f' % retangulo)
