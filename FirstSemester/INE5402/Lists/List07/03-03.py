# Prime Counter
# 6 of April of 2026


# Function to verify input
def verifica_entrada(x, start, end):
    if start <= x <= end:
        return x
    else:
        while True:
            x = int(input("Valor fora do limite, digite novamente: "))
            if start <= x <= end:
                break
    return x


# Verify if prime function
def verify_prime(x):
    prime = True
    for num in range(2, int(x / 2 + 1)):
        # If logic and break
        if x % num == 0:
            prime = False
            break
    return prime


s = 0

for i in range(0, 10):
    n = verifica_entrada(int(input("Digite N: ")), 2, 300)
    s += verify_prime(n)

print(s)
