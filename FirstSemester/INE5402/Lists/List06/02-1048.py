# Salary increase
# 6 of Abril of 2026


# Function to calculate salary increase
def calcula_aumento(salario):
    # If logic
    if salario <= 400:
        newsalario = salario * 1.15
        percent = 15
    elif salario <= 800:
        newsalario = salario * 1.12
        percent = 12
    elif salario <= 1200:
        newsalario = salario * 1.10
        percent = 10
    elif salario <= 2000:
        newsalario = salario * 1.07
        percent = 7
    else:
        newsalario = salario * 1.04
        percent = 4

    # Print result
    print("Novo salario: %.2f" % newsalario)
    print("Reajuste ganho: %.2f" % (newsalario - salario))
    print("Em percentual: %d%%" % percent)


calcula_aumento(float(input("Digite o salário: ")))
