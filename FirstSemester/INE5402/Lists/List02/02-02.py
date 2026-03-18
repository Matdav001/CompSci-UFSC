# Payment conditions
# 16 of March of 2026

# Variables declaration
price = float(input('Valor do produto: '))
condition = int(input('Condição do pagamento: '))

# If logic
if condition == 0:
    value = price * 0.9
elif condition == 1:
    value = price * 0.95
elif condition == 2:
    value = price
else:
    value = price * 1.2

# Print result
print('Preço a ser pago: R$ %.2f' % value)

# Print condition
if condition == 0:
    print('À vista')
else:
    print('Em %dx no cartão' % condition)