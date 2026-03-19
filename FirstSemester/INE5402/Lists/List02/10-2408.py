# Vice champion
# 16 of March of 2026

# Variables declaration
a, b, c = input('Pontos: ').split()

# Variables conversion
a, b, c = int(a), int(b), int(c)

# If logic and print result
if c < a < b or b < a < c:
    print (a)
if a < b < c or c < b < a:
    print (b)
if b < c < a or a < c < b:
    print (c)
