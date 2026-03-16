# Payment conditions
# 16 of March of 2026

# Variables declaration
PRICE = float(input('Valor do produto: '))
CONDITION = int(input('Condição do pagamento: '))

# If logic
if CONDITION == 0:
    VALUE = PRICE * 0.9
elif CONDITION == 1:
    VALUE = PRICE * 0.95
elif CONDITION == 2:
    VALUE = PRICE
elif CONDITION >= 3:
    VALUE = PRICE * 1.2

# Print result
print('Preço a ser pago: R$ %.2f' % VALUE)

# Print condition
if CONDITION == 0:
    print('À vista')
else:
    print('Em %dx no cartão' % CONDITION)