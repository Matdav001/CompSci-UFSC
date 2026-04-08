# Grandpa`s money
# 1 of April of 2026

# Variable declaration

n, s = input("Digite N e Saldo: ").split()
n, s = int(n), int(s)
low = s

# For loop
for i in range(0, n):
    movement = int(input("Digite a movimentação: "))
    s += movement

    # Get lowest value
    if s < low:
        low = s

    # Print result
print(low)
