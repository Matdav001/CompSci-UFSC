# Age in days
# 15 of March of 2026

# Variables declaration
age = int(input('Idade: '))

# Age calculation
ano = int(age / 365)
mes = int(age % 365 / 30)
dias = age % 365 % 30

# Print result
print(ano, 'ano(s)')
print(mes, 'mes(es)')
print(dias, 'dia(s)')
