# Mattress
# 6 of April of 2026


# Function to verify input
def verifica_entrada(x, start, end):
    if start <= x <= end:
        return x
    else:
        while True:
            x = int(input("Valor fora do limite, digite novamente: "))
            if start <= x <= end:
                break
    return x


# Function that calculates the mattress size
def colchao_cabe(a, b, c, h, l):
    # If logic and print result
    if (a <= h and b <= l) or (b <= h and a <= l):
        return True
    elif (b <= h and c <= l) or (c <= h and b <= l):
        return True
    elif (c <= h and a <= l) or (a <= h and c <= l):
        return True
    else:
        return False


# Variables declaration and verification
a = verifica_entrada(int(input("Digite a: ")), 1, 300)
b = verifica_entrada(int(input("Digite b: ")), 1, 300)
c = verifica_entrada(int(input("Digite c: ")), 1, 300)
h = verifica_entrada(int(input("Digite h: ")), 1, 250)
l = verifica_entrada(int(input("Digite l: ")), 1, 250)

# Verify result and print message
if colchao_cabe(a, b, c, h, l):
    print("Tamanho correto, parabéns")
else:
    print("Tamanho incorreto")
