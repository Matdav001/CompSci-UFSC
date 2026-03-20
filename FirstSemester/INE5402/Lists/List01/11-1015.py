# Distance between two points
# 15 of March of 2026

# Variables declaration
x1, y1 = input('Primeiro ponto: ').split()
x2, y2 = input('Segundo ponto: ').split()

# Variables conversion
x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

# Distance calculation
dist = (((x2-x1)**2)+((y2-y1)**2))**0.5

# Print result
print('%.4f' % dist)
