# Mean Bigger and Smaller
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
