# Mattress
# 18 of March of 2026

# Variables declaration
a, b, c, d = input('Valores: ').split()

# Variable conversion
a, b, c, d = int(a), int(b), int(c), int(d)

# If logic and print result
if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
