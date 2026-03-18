# Mattress
# 18 of March of 2026

# Variables declaration
a, b, c, d = input('Valores: ').split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

# If logic and print result
if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print('Valores nao aceitos')
else:
    print('Valores aceitos')