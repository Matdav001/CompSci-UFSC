# Mean 1
# 16 of March of 2026

# Variables declaration
N1 = float(input('Primeira nota: '))
N2 = float(input('Segunda nota: '))
N3 = float(input('Terceira nota: '))

# Mean calculation
MEDIA = (N1 + N2 + N3) / 3

# If logic and print result
if MEDIA < 5:
    print('Reprovado')
elif MEDIA < 7:
    print('Em recuperação')
else:
    print('Aprovado')