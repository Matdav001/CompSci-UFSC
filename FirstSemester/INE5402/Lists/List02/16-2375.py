# Ball Sedex
# 18 of March of 2026

# Variables declaration
d = int(input('Diâmetro da bola : '))
a, l, p = input('Dimensões da caixa: ').split()

# Variable conversion
a, l, p = int(a), int(l), int(p)

# If logic and print result
if d <= a and d <= l and d <= p:
    print('S')
else:
    print('N')
