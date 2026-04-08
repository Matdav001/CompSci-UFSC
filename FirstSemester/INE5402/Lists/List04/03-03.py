# Salary discount
# 30 of March of 2026

# Variable declaration
quitCode = "Y"

# While loop
while quitCode != "N":
    # Variable declaration
    num = 1
    salary = int(input("Digite o salário: "))
    if salary * 0.11 >= 320:
        print("Desconto de R$ 320,00 reais, sendo %.2f%% do salario" % (32000 / salary))
    else:
        print("Desconto de R$ %.2f reais, sendo 11%% do salario" % (salary * 0.11))
    # Verify stop condition
    quitCode = input("Continuar [Y/n]? ").upper()
