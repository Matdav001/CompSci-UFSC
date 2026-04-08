#
#
# List05
#
#

'''
#
# ============== EXERCISE: 01-01 ==============#
# Rock, Paper and Scissors
# 1 of April of 2026

# Variable declaration
quitCode = "Y"

# While loop
while quitCode != "N":
    # Variable declaration
    player1 = input("Jogador 1: ").upper()
    player2 = input("Jogador 2: ").upper()
    vic = 0

    # If logic
    if player1 == "PEDRA" and player2 == "TESOURA":
        vic = 1
    elif player1 == "TESOURA" and player2 == "PAPEL":
        vic = 1
    elif player1 == "PAPEL" and player2 == "PEDRA":
        vic = 1
    elif player2 == "PEDRA" and player1 == "TESOURA":
        vic = 2
    elif player2 == "TESOURA" and player1 == "PAPEL":
        vic = 2
    elif player2 == "PAPEL" and player1 == "PEDRA":
        vic = 2
    else:
        vic = 0

    # Print result
    if vic != 0:
        print("Vitória do player %d" % vic)
    else:
        print("Empate")

    # Verify stop condition
    quitCode = input("Continuar [Y/n]? ").upper()

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 02-02 ==============#
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

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 03-1150 =============#
# Overtaking Z
# 1 of April of 2026

# Variable declarations
x = int(input("Digite X: "))
z = int(input("Digite Z: "))
x_sum = 0
i = 0

# While loop
while True:
    # Verify Z and sum with x
    if z < x:
        z = int(input("Digite Z: "))
    if z > x:
        x_sum += x + i
    i += 1
    # Break if overtaken Z
    if x_sum > z:
        break

# Print retult
print(i)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 04-2454 =============#
# Flipper
# 1 of April of 2026

# Variables declaration
p = int(input("Digite P: "))
r = int(input("Digite R: "))

# If logic and print result
if p == 0:
    print("C")
elif r == 0:
    print("B")
else:
    print("A")

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 05-2373 =============#
# Waiter
# 1 of April of 2026

# Variable declaration
quitCode = "Y"
num = 0
number = int(input("Digite o número: "))
sum = 0

# While loop
while num < number:
    # Variable declaration
    l, c = input("Digite o número: ").split()
    l, c = int(l), int(c)

    # Sum calculation
    if l > c:
        sum += c

    # Update loop number
    num += 1

# Print result
print(sum)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 06-2295 =============#
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

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 07-1247 =============#
# Coast Guard
# 1 of April of 2026

# While loop
while True:
    # Variable declaration
    d, vf, vg = input("Digite D, Vf e Vg: ").split()
    d, vf, vg = int(d), int(vf), int(vg)

    # Max Distance calculation
    hipo = (d**2 + 144) ** 0.5

    # Speed logic
    if vf >= vg:
        print("N")
    # Speed distance logic
    elif (12 / vf) < (hipo / vg):
        print("N")
    else:
        print("S")

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 08-2434 =============#
# Grandpa`s money
# 1 of April of 2026

# Variable declaration

n, s = input("Digite N e Saldo: ").split()
n, s = int(n), int(s)
low = s

# For loop
for i in range(0, n):
    movement = int(input("Digite a movimentação: "))
    s += movement

    # Get lowest value
    if s < low:
        low = s

    # Print result
print(low)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 09-2297 =============#
# Card game
# 1 of April of 2026

# Variable declaration
round = 1

# While loop
while True:
    # Variable declaration
    r = int(input("Digite R: "))
    if r == 0:
        break
    a_total = 0
    b_total = 0

    for i in range(0, r):
        a, b = input("Digite A e B: ").split()
        a, b = int(a), int(b)
        a_total += a
        b_total += b

    print("Teste %d" % round)
    round += 1

    if a_total > b_total:
        print("Aldo")
    else:
        print("Beto")

#
# ==================== END ====================#
'''


