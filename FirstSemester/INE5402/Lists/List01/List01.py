#
#
# List01
#
#

'''
#
# ============= EXERCISE: 01-1003 =============#
# Simple sum
# 15 of March of 2026

# Variables declaration
a = int(input('Variável A: '))
b = int(input('Variável B: '))

# Sum calculation
soma = a + b

# Print result
print('SOMA =', soma)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 02-1004 =============#
# Simple product
# 15 of March of 2026

# Variables declaration
a = int(input('Variável A: '))
b = int(input('Variável B: '))

# Product calculation
prod = a * b

# Print result
print('PROD =', prod)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 03-1005 =============#
# Mean 1
# 15 of March of 2026

# Variables declaration
a = float(input('Variável A: '))
b = float(input('Variável B: '))

# Mean calculation
media = ((a * 3.5) + (b * 7.5)) / 11

# Print result
print('MEDIA = %.5f' % media)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 04-1006 =============#
# Mean 2
# 15 of March of 2026

# Variables declaration
a = float(input('Variável A: '))
b = float(input('Variável B: '))
c = float(input('Variável C: '))

# Mean calculation
media = ((a * 2) + (b * 3) + (c * 5)) / 10

# Print result
print('MEDIA = %.1f' % media)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 05-1007 =============#
# Difference
# 15 of March of 2026

# Variables declaration
a = int(input('Variável A: '))
b = int(input('Variável B: '))
c = int(input('Variável C: '))
d = int(input('Variável D: '))

# Difference calculation
diferenca =  (a * b - c * d)

# Print result
print('DIFERENCA =', diferenca)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 06-1008 =============#
# Salary
# 15 of March of 2026

# Variables declaration
num = int(input('Numero do funcionário: '))
hours = int(input('Horas trabalhadas: '))
value = float(input('Valor por hora: '))

# Salary calculation
salario = hours * value

# Print result
print('NUMBER =', num)
print('SALARY = U$ %.2f' % salario)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 07-2374 =============#
# Tire
# 15 of March of 2026

# Variables declaration
n = int(input('Variável N: '))
m = int(input('Variável M: '))

# Difference calculation
pressurediff = n - m

# Print result
print(pressurediff)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 08-2413 =============#
# Internet search
# 15 of March of 2026

# Variables declaration
t = int(input('Variável t: '))

# Product calculation
firstlink = t*4

# Print result
print(firstlink)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 09-1012 =============#
# Area
# 15 of March of 2026

# Variables declaration
a, b, c = input('Áreas: ').split()

# Variables conversion
a, b, c = float(a), float(b), float(c)

# Area calculation
triangulo = (a * c) / 2
circulo = 3.14159 * (c ** 2)
trapezio = ((a + b) * c) / 2
quadrado = b ** 2
retangulo = a * b

# Print result
print('TRIANGULO: %.3f' % triangulo)
print('CIRCULO: %.3f' % circulo)
print('TRAPEZIO: %.3f' % trapezio)
print('QUADRADO: %.3f' % quadrado)
print('RETANGULO: %.3f' % retangulo)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 10-1020 =============#
# Age in days
# 15 of March of 2026

# Variables declaration
age = int(input('Idade: '))

# Age calculation
ano = int(age / 365)
mes = int(age % 365 / 30)
dias = age % 365 % 30

# Print result
print(ano, 'ano(s)')
print(mes, 'mes(es)')
print(dias, 'dia(s)')

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 11-1015 =============#
# Distance between two points
# 15 of March of 2026

# Variables declaration
x1, y1 = input('Primeiro ponto: ').split()
x2, y2 = input('Segundo ponto: ').split()

# Variables conversion
x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

# Distance calculation
dist = (((x2-x1)**2)+((y2-y1)**2))**0.5

# Print result
print('%.4f' % dist)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 12-1019 =============#
# Time conversion
# 15 of March of 2026

# Variables declaration
n = int(input('Variável N: '))

# Time calculation
hora = int(n / 3600)
min = int(n % 3600 / 60 )
seg = n % 60 % 60

# Print result
print('%d:%d:%d' % (hora, min, seg))

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 13-1017 =============#
# Fuel consumption
# 15 of March of 2026

# Variables declaration
t = int(input('Tempo de viagem: '))
v = int(input('Velocidade média: '))

# Liters calculation
litros = (t*v)/12

# Print result
print('%.3f' % litros)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 14-1014 =============#
# Consumption
# 15 of March of 2026

# Variables declaration
x = int(input('Variável X: '))
y = float(input('Variável Y: '))

# Consumption calculation
cons = x/y 

# Print result
print('%.3f km/l' % cons)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 15-1009 =============#
# Salary with bonus
# 15 of March of 2026

# Variables declaration
name = input('Nome: ')
salary = float(input('Salário: '))
sales = float(input('Total de vendas: '))

# Final salary calculation
money = salary + (sales*0.15)

# Print result
print('TOTAL = R$ %.2f' % money)

#
# ==================== END ====================#
'''


