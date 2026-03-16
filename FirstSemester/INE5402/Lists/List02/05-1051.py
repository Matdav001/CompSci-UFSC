# Income tax
# 16 of March of 2026

# Variables declaration
RENDA = float(input('Salário: '))

# If logic
if RENDA <= 2000:
    # Print result
    print('Isento')

elif RENDA <= 3000:
    # Tax calculation
    IMPOSTO = (RENDA - 2000) * 0.08
    # Print result
    print('R$ %.2f' % IMPOSTO)

elif RENDA <= 4500:
    # Tax calculation
    IMPOSTO = (RENDA - 3000) * 0.18 + 80
    # Print result
    print('R$ %.2f' % IMPOSTO)

else:
    # Tax calculation
    IMPOSTO = (RENDA - 4500) * 0.28 + 80 + 270
    # Print result
    print('R$ %.2f' % IMPOSTO)