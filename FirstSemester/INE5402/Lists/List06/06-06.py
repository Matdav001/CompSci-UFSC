# Whole numbers
# 6 of April of 2026


# Function definition
def is_par(x):
    return "Ímpar" if x % 2 else "Par"


# Variable declaration
par = 0
impar = 0

# Values loop
for i in range(0, 10):
    if is_par(int(input("Digite o número: "))) == "Par":
        par += 1
    else:
        impar += 1

# Print result
print("Par: %d" % par)
print("Ímpar: %d" % impar)
