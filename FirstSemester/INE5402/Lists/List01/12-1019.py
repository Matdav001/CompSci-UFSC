# Time conversion
# 15 of March of 2026

# Variables declaration
N = int(input('Variável N: '))

# Time calculation
HORA = int(N / 3600)
MIN = int(N % 3600 / 60 )
SEG = N % 60 % 60

# Print result
print('%d:%d:%d' % (HORA, MIN, SEG))
