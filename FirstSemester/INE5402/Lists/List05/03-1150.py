# Overtaking Z
# 1 of April of 2026

# Variable declarations
x = int(input("Digite X: "))
z = int(input("Digite Z: "))
x_sum = 0
i = 0

# While loop
while True:
    # Verify Z and sum with x
    if z < x:
        z = int(input("Digite Z: "))
    if z > x:
        x_sum += x + i
    i += 1
    # Break if overtaken Z
    if x_sum > z:
        break

# Print retult
print(i)
