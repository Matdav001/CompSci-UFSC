# Name and discount
# 25 of March of 2026

# Variable declaration
name: str = ""
grade: float = 0
cost: float = 0

# For loop
for student in range(0, 5):
    # Variable declaration
    newname = input("Nome: ")
    newgrade = float(input("Nota: "))
    newcost = float(input("Valor da mensalidade: "))
    # If logic
    if newgrade > grade:
        grade = newgrade
        name = newname
        cost = newcost

# Print result
print("Nome:", name)
print("Mensalidade sem desconto:", cost)
print("Mensalidade com desconto:", cost * 0.7)
