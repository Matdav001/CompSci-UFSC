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
