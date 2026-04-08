# Elevator capacity control
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


# Function to control capacity
def controle_capacidade():
    overweight = False
    people = 0
    for i in range(0, n):
        s = verifica_entrada(int(input("Digite s: ")), 0, 1000)
        e = verifica_entrada(int(input("Digite e: ")), 0, 1000)
        people -= s
        people += e
        if people > c:
            overweight = True
    if overweight:
        print("S")
    else:
        print("N")


# Variable declaration
n = verifica_entrada(int(input("Digite N: ")), 1, 1000)
c = verifica_entrada(int(input("Digite C: ")), 1, 1000)

# Function call
controle_capacidade()
