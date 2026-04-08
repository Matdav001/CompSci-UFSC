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
