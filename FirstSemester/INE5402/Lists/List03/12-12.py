# Beaches distance
# 25 of March of 2026

# Variable declaration
beaches = int(input("Número de praias: "))
beach_name: str = ""
big_distance: int = 0
distant_beaches = 0
mean: float = 0

# For loop
for i in range(0, beaches):
    # Variable declaration
    name = input("Nome: ")
    num = int(input("Distancia: "))
    # If logic
    mean = mean + num
    if num > 15 and num < 20:
        distant_beaches += 1
    if num > big_distance:
        beach_name = name
        big_distance = num

# Print result
print("Praia mais distante: ", beach_name)
print("Praias entre 15km e 20km: ", distant_beaches)
print("Media: %.2f" % (mean / beaches))
