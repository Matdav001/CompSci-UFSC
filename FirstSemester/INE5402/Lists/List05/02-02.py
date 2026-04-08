# Sort Numbers
# 1 of April of 2026

# Variable declaration
n1, n2, n3 = input("Digite tres números: ").split()
n1, n2, n3 = int(n1), int(n2), int(n3)

# Sort logic with if
if n2 < n1:
    n1, n2 = n2, n1
if n3 < n2:
    n2, n3 = n3, n2
if n2 < n1:
    n1, n2 = n2, n1

# Print result
print(n1, n2, n3)
