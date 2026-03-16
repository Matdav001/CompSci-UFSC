# Distance between two points
# 15 of March of 2026

# Variables declaration
X1, Y1 = input('Primeiro ponto: ').split()
X2, Y2 = input('Segundo ponto: ').split()

# Variables conversion
X1 = float(X1)
Y1 = float(Y1)
X2 = float(X2)
Y2 = float(Y2)

# Distance calculation
DIST = (((X2-X1)**2)+((Y2-Y1)**2))**0.5

# Print result
print('%.4f' % DIST)
