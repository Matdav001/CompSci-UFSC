# Income tax
# 16 of March of 2026

# Variables declaration
renda = float(input('Salário: '))

# If logic
if renda <= 2000:
    # Print result
    print('Isento')

elif renda <= 3000:
    # Tax calculation
    imposto = (renda - 2000) * 0.08
    # Print result
    print('R$ %.2f' % imposto)

elif renda <= 4500:
    # Tax calculation
    imposto = (renda - 3000) * 0.18 + 80
    # Print result
    print('R$ %.2f' % imposto)

else:
    # Tax calculation
    imposto = (renda - 4500) * 0.28 + 80 + 270
    # Print result
    print('R$ %.2f' % imposto)
