# Fast food
# 18 of March of 2026

# Variables declaration
code, quantity = input('Código e quantidade: ').split()

code = float(code)
quantity = int(quantity)

# If logic
match code:
    case 1:
        total = 4 * quantity
    case 2:
        total = 4.5 * quantity
    case 3:
        total = 5 * quantity
    case 4:
        total = 2 * quantity
    case 5:
        total = 1.5 * quantity

# Print result
print('Total: R$ %.2f' % total)