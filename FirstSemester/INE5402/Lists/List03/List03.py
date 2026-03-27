#
#
# List03
#
#

'''
#
# ============== EXERCISE: 01-01 ==============#
# Leap year
# 25 of March of 2026

# For loop
for year in range(2001, 2100):
    # If logic and print result
    if year % 4 == 0:
        print(year)

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 02-02 ==============#
# Odd Number
# 25 of March of 2026

# For loop
for num in range(1, 50):
    # If logic and print result
    if num % 2 != 0:
        print(num)

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 03-03 ==============#
# Name and discount
# 25 of March of 2026

# Variable declaration
name: str = ""
grade: float = 0
cost: float = 0

# For loop
for student in range(0, 5):
    # Variable declaration
    newname = input("Nome: ")
    newgrade = float(input("Nota: "))
    newcost = float(input("Valor da mensalidade: "))
    # If logic
    if newgrade > grade:
        grade = newgrade
        name = newname
        cost = newcost

# Print result
print("Nome:", name)
print("Mensalidade sem desconto:", cost)
print("Mensalidade com desconto:", cost * 0.7)

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 04-04 ==============#
# Odd and even number
# 25 of March of 2026

# Variable declaration
even: int = 0
odd: int = 0

# For loop
for i in range(0, 10):
    # Variable declaration
    number = int(input("Number: "))
    # If logic
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

# Print result
print("Par:", even)
print("Ímpar:", odd)

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 05-05 ==============#
# Prime number
# 25 of March of 2026

# Variable declaration
number = int(input("Número: "))
prime = True

# For loop
for num in range(2, int(number / 2 + 1)):
    # If logic and break
    if number % num == 0:
        prime = False
        break

# If logic and print result
if prime == False:
    print("Não é primo")
else:
    print("É primo")

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 06-06 ==============#
# Prime number and factors
# 25 of March of 2026

# Variable declaration
number = int(input("Número: "))
prime = True

# For loop
for num in range(2, int(number / 2 + 1)):
    # If logic and break
    if number % num == 0:
        prime = False
        print(num)

# If logic and print result
if prime == False:
    print("Não é primo")
else:
    print("É primo")

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 07-07 ==============#
# Age mean
# 25 of March of 2026

# Variable declaration
number = int(input("Número de pessoas: "))
age: int = 0

# For loop
for num in range(0, number):
    age += int(input("Idade: "))

# Mean calculation
mean = age / number

# If logic and print result
if mean <= 25:
    print("Joven")
elif mean <= 60:
    print("Adulta")
else:
    print("Idosa")

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 08-08 ==============#
# Sum and Product
# 25 of March of 2026

# Variable declaration
start = int(input("Começo: "))
end = int(input("Final: "))
product: int = start
sum: int = 0

# For loop
for num in range(start, end + 1):
    # Sum and product calculation
    sum = sum + num
    product = product * num

# Print result
print("Soma: ", sum)
print("Produto: ", product)

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 09-09 ==============#
# Multiplication table
# 25 of March of 2026

# Variable declaration
number = int(input("Número: "))

# For loop
for num in range(1, 11):
    # Print result
    print("- %d x %d = %d" % (number, num, num * number))

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 10-10 ==============#
# Mean and approved status
# 25 of March of 2026

# Variable declaration
name: str = ""
grade: float = 0
sum: float = 0

# For loop
for student in range(0, 5):
    # Variable declaration
    newname = input("Nome: ")
    newgrade = float(input("Nota: "))
    sum = sum + newgrade
    # If logic
    if newgrade > grade:
        grade = newgrade
        name = newname

# Print result
print("Media:", sum / 5)
print("Nome:", name)

# If logic and print result
if grade >= 5.75:
    print("Aprovado")
elif grade >= 2.75:
    print("Em recuperação")
else:
    print("Reprovado")

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 11-11 ==============#
# Mean, bigger and smaller
# 25 of March of 2026

# Variable declaration
number = int(input("Número de variáveis: "))
mean: float = 0

# For loop
for i in range(0, number):
    # Variable declaration
    num = int(input("Número: "))
    # If logic
    mean = mean + num
    if i == 0:
        smaller = num
        bigger = num
    if num < smaller:
        smaller = num
    if num > bigger:
        bigger = num

# Print result
print("Menor: ", smaller)
print("Maior: ", bigger)
print("Media: ", mean / number)

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 12-12 ==============#
# Beaches distance
# 25 of March of 2026

# Variable declaration
beaches = int(input("Número de praias: "))
beach_name: str = ""
big_distance: int = 0
distant_beaches = 0
mean: float = 0

# For loop
for i in range(0, beaches):
    # Variable declaration
    name = input("Nome: ")
    num = int(input("Distancia: "))
    # If logic
    mean = mean + num
    if num > 15 and num < 20:
        distant_beaches += 1
    if num > big_distance:
        beach_name = name
        big_distance = num

# Print result
print("Praia mais distante: ", beach_name)
print("Praias entre 15km e 20km: ", distant_beaches)
print("Media: %.2f" % (mean / beaches))

#
# ==================== END ====================#
'''


