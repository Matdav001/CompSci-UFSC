# Taxi Fleet
# 1 of April of 2026

# Variable declaration
a, g, ra, rg = input("Digite o número: ").split()
a, g, ra, rg = float(a), float(g), float(ra), float(rg)

# If logic and print result
if (a / ra) >= (g / rg):
    print("G")
else:
    print("A")
