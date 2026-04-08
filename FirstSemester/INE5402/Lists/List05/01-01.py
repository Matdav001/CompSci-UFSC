# Rock, Paper and Scissors
# 1 of April of 2026

# Variable declaration
quitCode = "Y"

# While loop
while quitCode != "N":
    # Variable declaration
    player1 = input("Jogador 1: ").upper()
    player2 = input("Jogador 2: ").upper()
    vic = 0

    # If logic
    if player1 == "PEDRA" and player2 == "TESOURA":
        vic = 1
    elif player1 == "TESOURA" and player2 == "PAPEL":
        vic = 1
    elif player1 == "PAPEL" and player2 == "PEDRA":
        vic = 1
    elif player2 == "PEDRA" and player1 == "TESOURA":
        vic = 2
    elif player2 == "TESOURA" and player1 == "PAPEL":
        vic = 2
    elif player2 == "PAPEL" and player1 == "PEDRA":
        vic = 2
    else:
        vic = 0

    # Print result
    if vic != 0:
        print("Vitória do player %d" % vic)
    else:
        print("Empate")

    # Verify stop condition
    quitCode = input("Continuar [Y/n]? ").upper()
