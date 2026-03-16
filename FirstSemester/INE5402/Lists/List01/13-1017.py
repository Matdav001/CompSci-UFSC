# Fuel consuption
# 15 of March of 2026

# Variables declaration
T = int(input('Tempo de viagem: '))
V = int(input('Velocidade média: '))

# Liters calculation
LITROS = (T*V)/12

# Print result
print('%.3f' % LITROS)
