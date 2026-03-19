# Change
# 18 of March of 2026

# Variables declaration
price = float(input('Preço: '))
paid = float(input('Valor pago: '))

# If logic and print result
if price > paid:
    print('Faltando R$: %.2f' % (price - paid))
elif price == paid:
    print('Preço exato')
else:
    print('Troco R$: %.2f' % (price - paid))
