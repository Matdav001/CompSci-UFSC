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
