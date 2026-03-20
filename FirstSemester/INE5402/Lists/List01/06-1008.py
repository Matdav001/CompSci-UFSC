# Salary
# 15 of March of 2026

# Variables declaration
num = int(input('Numero do funcionário: '))
hours = int(input('Horas trabalhadas: '))
value = float(input('Valor por hora: '))

# Salary calculation
salario = hours * value

# Print result
print('NUMBER =', num)
print('SALARY = U$ %.2f' % salario)
