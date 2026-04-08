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
