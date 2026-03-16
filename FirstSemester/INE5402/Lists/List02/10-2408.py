# Vice champion
# 16 of March of 2026

# Variables declaration
A, B, C = input('Notas: ').split()

# Variables conversion
A = float(A)
B = float(B)
C = float(C)

if A < B and B < C:
    print (B)
if B < C and C < A or B < C and C < A:
    print (C)