# Salary
# 15 of March of 2026

# Variables declaration
NUM = int(input('Numero do funcionário: '))
HOURS = int(input('Horas trabalhadas: '))
VALUE = float(input('Valor por hora: '))

# Salary calculation
SALARIO = HOURS * VALUE

# Print result
print('NUMBER =', NUM)
print('SALARY = U$ %.2f' % SALARIO)
