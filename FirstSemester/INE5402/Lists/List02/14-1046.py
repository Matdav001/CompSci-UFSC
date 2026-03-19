# Game time
# 18 of March of 2026

# Variables declaration
hinit, hfim = input('Hora inicial e final: ').split()

# Variable conversion
hinit, hfim = int(hinit), int(hfim)

# Points calculation
hours = hfim - hinit

# If logic
if hours < 0:
    hours = 24 + hours
if hours == 0:
    hours = 24

# Print result
print('O JOGO DUROU %d HORA(S)' % hours)
