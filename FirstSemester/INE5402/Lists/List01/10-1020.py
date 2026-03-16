# Age in days
# 15 of March of 2026

# Variables declaration
AGE = int(input('Idade: '))

# Age calculation
ANO = int(AGE / 365)
MES = int(AGE % 365 / 30)
DIAS = AGE % 365 % 30

# Print result
print(ANO, 'ano(s)')
print(MES, 'mes(es)')
print(DIAS, 'dia(s)')
