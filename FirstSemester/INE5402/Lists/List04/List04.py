#
#
# List04
#
#

'''
#
# ============== EXERCISE: 01-01 ==============#
# Sex selection
# 25 of March of 2026

# While loop
while True:
    # Variable declaration
    sex = input("Digite o Sexo: ")
    # If logic and print result
    if sex != "M" and sex != "F":
        print("Seleção errada, digite apenas F ou M")
    else:
        break

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 02-02 ==============#
# Random game
# 25 of March of 2026

# Imports
import random

rand = random.randint(0, 10)
tries: int = 0

# While loop
while True:
    # Variable declaration
    tries += 1
    num = int(input("Digite o número: "))
    # If logic and print result
    if num != rand:
        print("Número errado")
    else:
        print("Voce Venceu em %d tentativas" % tries)
        break

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 03-03 ==============#
# Salary discount
# 30 of March of 2026

# Variable declaration
quitCode = "Y"

# While loop
while quitCode != "N":
    # Variable declaration
    num = 1
    salary = int(input("Digite o salário: "))
    if salary * 0.11 >= 320:
        print("Desconto de R$ 320,00 reais, sendo %.2f%% do salario" % (32000 / salary))
    else:
        print("Desconto de R$ %.2f reais, sendo 11%% do salario" % (salary * 0.11))
    # Verify stop condition
    quitCode = input("Continuar [Y/n]? ").upper()

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 04-1075 =============#
# Rest of division by 2
# 30 of March of 2026

# Variables declaration
num = int(1)
n = int(input("Digite o número: "))

# While loop
while num <= 10000:
    # If logic
    if num % n == 2:
        # Print result
        print(num)
    # Update loop number
    num += 1

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 05-1078 =============#
# Multiplication table
# 30 of March of 2026

# Variable declaration
quitCode = "Y"

# While loop
while quitCode != "N":
    # Variable declaration
    num = 1
    number = int(input("Digite o número: "))
    # While loop
    while num <= 10:
        # Print result
        print("%d x %d = %d" % (number, num, num * number))
        # Update loop number
        num += 1
    # Verify stop condition
    quitCode = input("Continuar [Y/n]? ").upper()

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 06-1146 =============#
# Crescent sequences
# 30 of March of 2026

# Variable declaration
number = 1

# While loop
while number != 0:
    # Variable declaration
    num = 1
    number = int(input("Digite o número: "))
    # While loop
    while num <= number:
        # If logic and print result
        if number == num:
            print(num)
        else:
            print(num, end=" ")
        # Update loop number
        num += 1

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 07-1134 =============#
# Fuel Type
# 30 of March of 2026

# Variable declaration
alcool = 0
gas = 0
diesel = 0

# While loop
while True:
    # Variable declaration
    num = 1
    number = int(input("Digite o número: "))
    # Case logic
    match number:
        case 1:
            alcool += 1
        case 2:
            gas += 1
        case 3:
            diesel += 1
        case 4:
            # Print result and stop code
            print("MUITO OBRIGADO")
            print("Alcool: %d" % alcool)
            print("Gasolina: %d" % gas)
            print("Diesel: %d" % diesel)
            break

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 08-1101 =============#
# Number sequences and sum
# 30 of March of 2026

# While loop
while True:
    # Variable declaration
    n = int(input("Digite N: "))
    m = int(input("Digite M: "))

    # If logic and break
    if m == 0:
        break
    if n > m:
        m, n = n, m

    # Sum calculation
    sum = 0

    # While loop
    while n <= m:
        # Print result
        print(n, end=" ")
        sum += n
        n += 1
    print("Sum=", sum, sep="")

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 09-1113 =============#
# Crescent and decrescent
# 30 of March of 2026

# While loop
while True:
    # Variable declaration
    x = int(input("Digite x: "))
    y = int(input("Digite y: "))

    # If logic and break
    if x == y:
        break

    # If logic and print result
    elif x > y:
        print("Decrescente")
    else:
        print("Crescente")

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 10-1099 =============#
# Sum of odds
# 30 of March of 2026

# Variables declaration
num = 1
n = int(input("Digite N: "))

# While loop
while num <= n:
    # Variable declaration
    x = int(input("Digite X: "))
    y = int(input("Digite Y: "))

    # If logic
    if x > y:
        y, x = x, y

    # Sum calculation
    sum = 0
    x += 1

    # While loop
    while x < y:
        if x % 2 != 0:
            sum += x
        x += 1

    # Print result
    print(sum)
    # Update loop number
    num += 1

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 11-11 ==============#
# Fibonacci
# 30 of March of 2026

# Variable declaration
num = 1
n = int(input("Digite N: "))
f1 = 1
f2 = 0
fib = 1

# Print the start of the Fibonacci sequence
if n >= 1:
    print(0, end="-")

# While loop
while num <= n - 1:
    # If logic and print result
    if n - 1 == num:
        print(fib)
    else:
        print(fib, end="-")

    # Fibonacci calculation
    fib = f1 + f2
    f2 = f1
    f1 = fib

    # Update loop number
    num += 1

#
# ==================== END ====================#
'''


