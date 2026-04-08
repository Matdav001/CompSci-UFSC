# Time zone
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


def fuso(s, t, f):
    print("Horario no destino: %d" % ((s + t + f) % 24))


# Variables declaration
s = verifica_entrada(int(input("Digite s: ")), 0, 23)
t = verifica_entrada(int(input("Digite t: ")), 1, 12)
f = verifica_entrada(int(input("Digite f: ")), -5, 5)

fuso(s, t, f)
