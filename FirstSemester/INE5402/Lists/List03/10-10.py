# Mean and approved status
# 25 of March of 2026

# Variable declaration
name: str = ""
grade: float = 0
sum: float = 0

# For loop
for student in range(0, 5):
    # Variable declaration
    newname = input("Nome: ")
    newgrade = float(input("Nota: "))
    sum = sum + newgrade
    # If logic
    if newgrade > grade:
        grade = newgrade
        name = newname

# Print result
print("Media:", sum / 5)
print("Nome:", name)

# If logic and print result
if grade >= 5.75:
    print("Aprovado")
elif grade >= 2.75:
    print("Em recuperação")
else:
    print("Reprovado")
