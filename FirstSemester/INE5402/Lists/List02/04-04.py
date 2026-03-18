# Mean 1
# 16 of March of 2026

# Variables declaration
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))

# Mean calculation
media = (n1 + n2 + n3) / 3

# If logic and print result
if media < 5:
    print('Reprovado')
elif media < 7:
    print('Em recuperação')
else:
    print('Aprovado')