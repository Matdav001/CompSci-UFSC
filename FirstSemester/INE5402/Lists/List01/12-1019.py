# Time conversion
# 15 of March of 2026

# Variables declaration
n = int(input('Variável N: '))

# Time calculation
hora = int(n / 3600)
min = int(n % 3600 / 60 )
seg = n % 60 % 60

# Print result
print('%d:%d:%d' % (hora, min, seg))
