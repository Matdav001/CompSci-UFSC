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
