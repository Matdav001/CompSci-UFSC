# Montlhy payment
# 16 of March of 2026

# Variables declaration
HOUSE = float(input('Valor da casa: '))
SALARY = float(input('Salário do comprador: '))
YEARS = int(input('Anos pagando: '))

# Distance calculation
PAYMENT = HOUSE / (YEARS * 12)

# If logic and print result
if PAYMENT <= SALARY * 0.3:
    print('R$ %.2f' % PAYMENT)
else:
    print('Pagamento negado')