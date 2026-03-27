# Sum and Product
# 25 of March of 2026

# Variable declaration
start = int(input("Começo: "))
end = int(input("Final: "))
product: int = start
sum: int = 0

# For loop
for num in range(start, end + 1):
    # Sum and product calculation
    sum = sum + num
    product = product * num

# Print result
print("Soma: ", sum)
print("Produto: ", product)
