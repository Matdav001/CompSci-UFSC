# Perfect number
# 11 of may of 2026

# Variables declaration
n = int(input("Digite N: "))

# Test case loop
for i in range(n):
    x = int(input("Digite X: "))
    s = 0
    i = 0
    # Logic loop
    while s < x:
        i += 1
        s += i
    # Print result
    if s == x:
        print("%d eh perfeito" % x)
    else:
        print("%d nao eh perfeito" % x)
