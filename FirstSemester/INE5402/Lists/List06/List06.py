#
#
# List06
#
#

'''
#
# ============== EXERCISE: 01-01 ==============#
# Area Function
# 6 of April of 2026


# Function to calculate area
def calcula_area(largura, comprimento):
    print("Área: %d" % (largura * comprimento))


# Variable definition
larg = int(input("Digite largura: "))
comp = int(input("Digite comprimento: "))

# Call function and print result
calcula_area(larg, comp)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 02-1048 =============#
# Salary increase
# 6 of Abril of 2026


# Function to calculate salary increase
def calcula_aumento(salario):
    # If logic
    if salario <= 400:
        newsalario = salario * 1.15
        percent = 15
    elif salario <= 800:
        newsalario = salario * 1.12
        percent = 12
    elif salario <= 1200:
        newsalario = salario * 1.10
        percent = 10
    elif salario <= 2000:
        newsalario = salario * 1.07
        percent = 7
    else:
        newsalario = salario * 1.04
        percent = 4

    # Print result
    print("Novo salario: %.2f" % newsalario)
    print("Reajuste ganho: %.2f" % (newsalario - salario))
    print("Em percentual: %d%%" % percent)


calcula_aumento(float(input("Digite o salário: ")))

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 03-03 ==============#
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

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 04-2057 =============#
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

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 05-2409 =============#
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

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 06-06 ==============#
# Whole numbers
# 6 of April of 2026


# Function definition
def is_par(x):
    return "Ímpar" if x % 2 else "Par"


# Variable declaration
par = 0
impar = 0

# Values loop
for i in range(0, 10):
    if is_par(int(input("Digite o número: "))) == "Par":
        par += 1
    else:
        impar += 1

# Print result
print("Par: %d" % par)
print("Ímpar: %d" % impar)

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 07-07 ==============#
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

#
# ==================== END ====================#
'''


