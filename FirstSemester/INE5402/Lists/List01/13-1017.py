# Fuel consumption
# 15 of March of 2026

# Variables declaration
t = int(input('Tempo de viagem: '))
v = int(input('Velocidade média: '))

# Liters calculation
litros = (t*v)/12

# Print result
print('%.3f' % litros)
