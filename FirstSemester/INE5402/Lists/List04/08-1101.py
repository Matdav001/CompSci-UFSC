# Number sequences and sum
# 30 of March of 2026

# While loop
while True:
    # Variable declaration
    n = int(input("Digite N: "))
    m = int(input("Digite M: "))

    # If logic and break
    if m == 0:
        break
    if n > m:
        m, n = n, m

    # Sum calculation
    sum = 0

    # While loop
    while n <= m:
        # Print result
        print(n, end=" ")
        sum += n
        n += 1
    print("Sum=", sum, sep="")
