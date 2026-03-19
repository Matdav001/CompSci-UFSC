# Bhaskara
# 16 of March of 2026

# Variables declaration
a, b, c = input('A, B e C: ').split()

# Variables conversion
a, b, c = float(a), float(b), float(c)

# Delta calculation
delta = (b**2) - (4 * a * c)

# If logic
if delta < 0 or a == 0:
    # Print result
    print('Impossivel calcular')
else:
    # Calculate roots
    r1 = (-b + delta ** 0.5)/(2*a)
    r2 = (-b - delta ** 0.5)/(2*a)
    # Print result
    print('R1 = %.5f' % r1)
    print('R2 = %.5f' % r2)
