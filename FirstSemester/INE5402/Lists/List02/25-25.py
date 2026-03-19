# Price discount
# 18 of March of 2026

# Variables declaration
price = float(input('Price: '))

# If logic
if price >= 7000:
    discount = price * 0.25
elif price >= 5000:
    discount = price * 0.15
else:
    discount = price * 0.05

# Print result
print('Valor da compra: %.2f' % (price))
print('Desconto obtido: %.2f' % (discount))
print('Valor da compra com desconto: %.2f' % (price - discount))
