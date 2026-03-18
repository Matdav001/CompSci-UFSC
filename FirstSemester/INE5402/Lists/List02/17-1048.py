# Salary raise
# 18 of March of 2026

# Variables declaration
salary = float(input('Salário: '))

# If logic
if salary <= 400:
    newsalary = salary * 1.15
    percent = 15
elif salary <= 800:
    newsalary = salary * 1.12
    percent = 12
elif salary <= 1200:
    newsalary = salary * 1.10
    percent = 10
elif salary <= 2000:
    newsalary = salary * 1.07
    percent = 7
else:
    newsalary = salary * 1.04
    percent = 4

# Print result
print('Novo salario: %.2f' % newsalary)
print('Reajuste ganho: %.2f' % (newsalary - salary))
print('Em percentual: %d%%' % percent)