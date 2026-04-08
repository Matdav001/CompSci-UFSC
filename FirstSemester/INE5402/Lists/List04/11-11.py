# Fibonacci
# 30 of March of 2026

# Variable declaration
num = 1
n = int(input("Digite N: "))
f1 = 1
f2 = 0
fib = 1

# Print the start of the Fibonacci sequence
if n >= 1:
    print(0, end="-")

# While loop
while num <= n - 1:
    # If logic and print result
    if n - 1 == num:
        print(fib)
    else:
        print(fib, end="-")

    # Fibonacci calculation
    fib = f1 + f2
    f2 = f1
    f1 = fib

    # Update loop number
    num += 1
