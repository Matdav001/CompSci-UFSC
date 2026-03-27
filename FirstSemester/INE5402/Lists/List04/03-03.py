# Random game
# 25 of March of 2026

# Imports
import random

rand = random.randint(0, 10)
tries: int = 0

# While loop
while True:
    # Variable declaration
    tries += 1
    num = int(input("Digite o número: "))
    # If logic and print result
    if num != rand:
        print("Número errado")
    else:
        print("Voce Venceu em %d tentativas" % tries)
        break
