# Salary with bonus
# 15 of March of 2026

# Variables declaration
name = input('Nome: ')
salary = float(input('Salário: '))
sales = float(input('Total de vendas: '))

# Final salary calculation
money = salary + (sales*0.15)

# Print result
print('TOTAL = R$ %.2f' % money)
