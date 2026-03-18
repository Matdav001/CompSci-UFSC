# Mattress
# 18 of March of 2026

# Variables declaration
a, b, c = input('Dimensões do colchão: ').split()
h, l = input('Dimensões da porta: ').split()

a = int(a)
b = int(b)
c = int(c)
h = int(h)
l = int(l)

# If logic and print result
if (a <= h and b <=l) or (b <= h and a <=l):
    print('S')
elif (b <= h and c <=l) or (c <= h and b <=l):
    print('S')
elif (c <= h and a <=l) or (a <= h and c <=l):
    print('S')
else:
    print('N')