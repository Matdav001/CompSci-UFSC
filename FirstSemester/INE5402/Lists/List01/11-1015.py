# Distance between two points
# 15 of March of 2026

# Variables declaration
pX1, pY1 = input('Primeiro ponto: ').split()
pX2, pY2 = input('Segundo ponto: ').split()

# Variables conversion
X1 = float(pX1)
Y1 = float(pY1)
X2 = float(pX2)
Y2 = float(pY2)

# Distance calculation
DIST = (((X2-X1)**2)+((Y2-Y1)**2))**0.5

# Print result
print('%.4f' % DIST)
