# Distance Traveled
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
def calcula_distância(tempo, velocidade):
    return tempo * velocidade


# Variable declaration
n = verifica_entrada(int(input("Digite N: ")), 1, 10)
distance = 0

# For loop
for i in range(0, n):
    tem = verifica_entrada(int(input("Digite T: ")), 0, 1000)
    vel = verifica_entrada(int(input("Digite V: ")), 0, 1000)
    distance += calcula_distância(tem, vel)

# Function call
print("Distância total percorrida: %d km considerando os %d trechos" % (distance, n))
