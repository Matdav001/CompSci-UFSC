# Sum and difference
# 6 of April of 2026


def sum_range(start, end):
    s = 0
    for i in range(start, end + 1):
        s += i
    return s


def diff(x, y):
    if x >= y:
        return x - y
    else:
        return y - x


# Variable declaration
quitCode = "Y"

# While loop
while quitCode != "N":
    # Variable declaration
    s_start, s_end = input("Digite o intervalo: ").split()
    s_start, s_end = int(s_start), int(s_end)
    print(sum_range(s_start, s_end))
    d1, d2 = input("Digite 2 valores: ").split()
    d1, d2 = int(d1), int(d2)
    print(diff(d1, d2))

    # Verify stop condition
    quitCode = input("Continuar [Y/n]? ").upper()
