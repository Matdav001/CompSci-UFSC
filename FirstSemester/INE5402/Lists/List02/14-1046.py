# Game time
# 18 of March of 2026

# Variables declaration
hinit, hfim = input('Hora inicial e final: ').split()

# Variables conversion
hinit = int(hinit)
hfim = int(hfim)

# Points calculation
hours = hfim - hinit

# If logic
if hours < 0:
    hours = 24 - hours
# Print result
print(hours)