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
