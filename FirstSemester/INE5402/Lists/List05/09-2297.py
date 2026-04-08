# Card game
# 1 of April of 2026

# Variable declaration
round = 1

# While loop
while True:
    # Variable declaration
    r = int(input("Digite R: "))
    if r == 0:
        break
    a_total = 0
    b_total = 0

    for i in range(0, r):
        a, b = input("Digite A e B: ").split()
        a, b = int(a), int(b)
        a_total += a
        b_total += b

    print("Teste %d" % round)
    round += 1

    if a_total > b_total:
        print("Aldo")
    else:
        print("Beto")
