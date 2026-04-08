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
