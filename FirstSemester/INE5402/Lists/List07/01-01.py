# Zero or One
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


# Function to print winner
def vencedor(a, b, c):
    if a != b == c:
        print("A")
    elif b != a == c:
        print("B")
    elif c != b == a:
        print("C")
    else:
        print("*")


# Variables declaration
while True:
    a = verifica_entrada(int(input("Digite A: ")), 0, 1)
    b = verifica_entrada(int(input("Digite B: ")), 0, 1)
    c = verifica_entrada(int(input("Digite C: ")), 0, 1)
    if a == b == c == 0:
        break
    vencedor(a, b, c)
