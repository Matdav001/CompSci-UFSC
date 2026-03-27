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
