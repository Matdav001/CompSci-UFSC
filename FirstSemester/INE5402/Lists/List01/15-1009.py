# Salary with bonus
# 15 of March of 2026

# Variables declaration
NAME = input('Nome: ')
SALARY = float(input('Salário: '))
SALES = float(input('Total de vendas: '))

# Final salary calculation
MONEY = SALARY + (SALES*0.15)

# Print result
print('TOTAL = R$ %.2f' % MONEY)
