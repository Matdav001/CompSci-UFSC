# Monthly payment
# 16 of March of 2026

# Variables declaration
house = float(input('Valor da casa: '))
salary = float(input('Salário do comprador: '))
years = int(input('Anos pagando: '))

# Distance calculation
payment = house / (years * 12)

# If logic and print result
if payment <= salary * 0.3:
    print('R$ %.2f' % payment)
else:
    print('Pagamento negado')
