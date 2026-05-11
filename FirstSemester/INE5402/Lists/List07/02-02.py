# Kite
# 8 of April of 2026


# Function to verify input
def verifica_entrada(x, start, end, char):
    if start <= x <= end:
        return x
    else:
        while True:
            x = int(input("Valor fora do limite, digite %s novamente: " % char))
            if start <= x <= end:
                break
    return x


# Variables declaration
n = int(input("Digite a quantidade de pipas: "))

# For loop
for i in range(0, n):
    # Variables declaration and validation
    x, y = input("Digite x e y: ").split()
    x, y = verifica_entrada(int(x), 1, 100, "x"), verifica_entrada(int(y), 1, 100, "y")

    # Print result and calculate area
    print("Área: %d cm2" % (x * y / 2))
