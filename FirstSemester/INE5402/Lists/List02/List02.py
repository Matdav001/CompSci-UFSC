#
#
# List02
#
#

'''
#
# ============== EXERCISE: 01-01 ==============#
# Monthly payment
# 16 of March of 2026

# Variables declaration
house = float(input('Valor da casa: '))
salary = float(input('Salário do comprador: '))
years = int(input('Anos pagando: '))

# Distance calculation
payment = house / (years * 12)

# If logic and print result
if payment <= salary * 0.3:
    print('R$ %.2f' % payment)
else:
    print('Pagamento negado')
#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 02-02 ==============#
# Payment conditions
# 16 of March of 2026

# Variables declaration
price = float(input('Valor do produto: '))
condition = int(input('Condição do pagamento: '))

# If logic
if condition == 0:
    value = price * 0.9
elif condition == 1:
    value = price * 0.95
elif condition == 2:
    value = price
else:
    value = price * 1.2

# Print result
print('Preço a ser pago: R$ %.2f' % value)

# Print condition
if condition == 0:
    print('À vista')
else:
    print('Em %dx no cartão' % condition)
#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 03-03 ==============#
# BMI calculation
# 16 of March of 2026

# Variables declaration
weight = float(input())
height = float(input())

# BMI calculation
imc = weight / (height ** 2)

# if logic and print result
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 04-04 ==============#
# Mean 1
# 16 of March of 2026

# Variables declaration
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))

# Mean calculation
media = (n1 + n2 + n3) / 3

# If logic and print result
if media < 5:
    print('Reprovado')
elif media < 7:
    print('Em recuperação')
else:
    print('Aprovado')
#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 05-1051 =============#
# Income tax
# 16 of March of 2026

# Variables declaration
renda = float(input('Salário: '))

# If logic
if renda <= 2000:
    # Print result
    print('Isento')

elif renda <= 3000:
    # Tax calculation
    imposto = (renda - 2000) * 0.08
    # Print result
    print('R$ %.2f' % imposto)

elif renda <= 4500:
    # Tax calculation
    imposto = (renda - 3000) * 0.18 + 80
    # Print result
    print('R$ %.2f' % imposto)

else:
    # Tax calculation
    imposto = (renda - 4500) * 0.28 + 80 + 270
    # Print result
    print('R$ %.2f' % imposto)
#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 06-1061 =============#
# Event time
# 16 of March of 2026

# Variables declaration
dia, diainit = (input('Dia de término: ')).split()
hinit, comma0, minit, comma1, sinit = input('Hora de começo: ').split()

# Variables conversion
diainit, hinit, minit, sinit= int(diainit), int(hinit), int(minit), int(sinit)

# Variables declaration
dia, diafim = (input('Dia de término: ')).split()
hfim, comma0, mfim, comma1, sfim = input('Hora de término: ').split()

# Variables conversion
diafim, hfim, mfim, sfim = int(diafim), int(hfim), int(mfim), int(sfim)

# Seconds calculation
sdiff = sfim - sinit

# Minutes calculation
if sdiff < 0:
    mdiff = mfim - minit - 1
    sdiff = 60 + sdiff
else:
    mdiff = mfim - minit

# Hours calculation
if mdiff < 0:
    hdiff = hfim - hinit - 1
    mdiff = 60 + mdiff
else:
    hdiff = hfim - hinit

# Days calculation
if hdiff < 0:
    diadiff = diafim - diainit - 1
    hdiff = 24 + hdiff
else:
    diadiff = diafim - diainit

# Print result
print(diadiff, 'dia(s)')
print(hdiff, 'hora(s)')
print(mdiff, 'minuto(s)')
print(sdiff, 'segundo(s)')

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 07-1050 =============#
# Area Code
# 16 of March of 2026

# Variables declaration
code = int(input('DDD: '))

# If logic and print result
match code:
    case 61:
        print('Brasilia')
    case 71:
        print('Salvador')
    case 11:
        print('Sao Paulo')
    case 21:
        print('Rio de Janeiro')
    case 32:
        print('Juiz de Fora')
    case 19:
        print('Campinas')
    case 27:
        print('Vitoria')
    case 31:
        print('Belo Horizonte')
    case _:
        print('DDD nao cadastrado')
#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 08-1052 =============#
# Month
# 16 of March of 2026

# Variables declaration
code = int(input('Mês: '))

# If logic and print result
match code:
    case 1:
        print('January')
    case 2:
        print('February')
    case 3:
        print('March')
    case 4:
        print('April')
    case 5:
        print('May')
    case 6:
        print('June')
    case 7:
        print('July')
    case 8:
        print('August')
    case 9:
        print('September')
    case 10:
        print('October')
    case 11:
        print('November')
    case 12:
        print('December')
    case _:
        print('Não existe')
#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 09-1036 =============#
# Bhaskara
# 16 of March of 2026

# Variables declaration
a, b, c = input('A, B e C: ').split()

# Variables conversion
a, b, c = float(a), float(b), float(c)

# Delta calculation
delta = (b**2) - (4 * a * c)

# If logic
if delta < 0 or a == 0:
    # Print result
    print('Impossivel calcular')
else:
    # Calculate roots
    r1 = (-b + delta ** 0.5)/(2*a)
    r2 = (-b - delta ** 0.5)/(2*a)
    # Print result
    print('R1 = %.5f' % r1)
    print('R2 = %.5f' % r2)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 10-2408 =============#
# Vice champion
# 16 of March of 2026

# Variables declaration
a, b, c = input('Pontos: ').split()

# Variables conversion
a, b, c = int(a), int(b), int(c)

# If logic and print result
if c < a < b or b < a < c:
    print (a)
if a < b < c or c < b < a:
    print (b)
if b < c < a or a < c < b:
    print (c)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 11-2417 =============#
# Soceer champion
# 18 of March of 2026

# Variables declaration
cv, ce, cs, fv, fe, fs = input('Números: ').split()

# Variables conversion
cv, ce, cs = int(cv), int(ce), int(cs)
fv, fe, fs = int(fv), int(fe), int(fs)

# Points calculation
cpoints = cv * 3 + ce
fpoints = fv * 3 + fe

# If logic and print result
if (cpoints > fpoints):
    print ('C')
elif (cpoints < fpoints):
    print ('F')
else:
    if (cs > fs):
        print ('C')
    if (cs < fs):
        print ('F')
    else:
        print ('=')

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 12-2600 =============#
# New die
# 18 of March of 2026
# Do not consider the number of cases

# Variables declaration
d1 = int(input())
d2, d3, d4, d5 = input().split()
d6 = int(input())

# Variables conversion
d2, d3, d4, d5 = int(d2), int(d3), int(d4), int(d5)

# If logic and print result
if d1 + d6 != 7:
    print('NAO')
elif d2 + d4 != 7:
    print('NAO')
elif d3 + d5 != 7:
    print('NAO')
else:
    print('SIM')

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 14-1046 =============#
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

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 15-1047 =============#
# Game time with minutes
# 18 of March of 2026

# Variables declaration
hinit, minit, hfim, mfim = input('Horario inicial e final: ').split()
 
# Variable conversion
hinit, minit, hfim, mfim = int(hinit), int(minit), int(hfim), int(mfim)

# Minutes calculation
mdiff = mfim - minit

# Hours calculation
if mdiff < 0:
    hdiff = hfim - hinit - 1
    mdiff = 60 + mdiff
else:
    hdiff = hfim - hinit

if hdiff == 0 and mdiff == 0:
    hdiff = 24
# Print result
print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' % (hdiff, mdiff))

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 16-2375 =============#
# Ball Sedex
# 18 of March of 2026

# Variables declaration
d = int(input('Diâmetro da bola : '))
a, l, p = input('Dimensões da caixa: ').split()

# Variable conversion
a, l, p = int(a), int(l), int(p)

# If logic and print result
if d <= a and d <= l and d <= p:
    print('S')
else:
    print('N')

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 17-1048 =============#
# Salary raise
# 18 of March of 2026

# Variables declaration
salary = float(input('Salário: '))

# If logic
if salary <= 400:
    newsalary = salary * 1.15
    percent = 15
elif salary <= 800:
    newsalary = salary * 1.12
    percent = 12
elif salary <= 1200:
    newsalary = salary * 1.10
    percent = 10
elif salary <= 2000:
    newsalary = salary * 1.07
    percent = 7
else:
    newsalary = salary * 1.04
    percent = 4

# Print result
print('Novo salario: %.2f' % newsalary)
print('Reajuste ganho: %.2f' % (newsalary - salary))
print('Em percentual: %d%%' % percent)
#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 18-2409 =============#
# Mattress
# 18 of March of 2026

# Variables declaration
a, b, c = input('Dimensões do colchão: ').split()
h, l = input('Dimensões da porta: ').split()

# Variable conversion
a, b, c = int(a), int(b), int(c)
h, l = int(h), int(l)


# If logic and print result
if (a <= h and b <=l) or (b <= h and a <=l):
    print('S')
elif (b <= h and c <=l) or (c <= h and b <=l):
    print('S')
elif (c <= h and a <=l) or (a <= h and c <=l):
    print('S')
else:
    print('N')

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 19-1035 =============#
# Mattress
# 18 of March of 2026

# Variables declaration
a, b, c, d = input('Valores: ').split()

# Variable conversion
a, b, c, d = int(a), int(b), int(c), int(d)

# If logic and print result
if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 20-1038 =============#
# Snack
# 18 of March of 2026

# Variables declaration
code, quantity = input('Código e quantidade: ').split()

# Variable conversion
code, quantity = float(code), int(quantity)

# If logic
match code:
    case 1:
        total = 4 * quantity
    case 2:
        total = 4.5 * quantity
    case 3:
        total = 5 * quantity
    case 4:
        total = 2 * quantity
    case 5:
        total = 1.5 * quantity
    case _:
        total = 0

# Print result
print('Total: R$ %.2f' % total)

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 21-2339 =============#
# Paper planes
# 18 of March of 2026

# Variables declaration
c, p, f = input('Alunos, folhas a folhas por aluno: ').split()

# Variable conversion
c, p, f = int(c), int(p), int(f)

# If logic and print result
if f * c <= p:
    print('S')
else:
    print('N')

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 22-1045 =============#
# Triangles types
# 18 of March of 2026

# Variables declaration
a, b, c = input('Dimensões do triângulo: ').split()

# Variable conversion
a, b, c = float(a), float(b), float(c)

# Sort decrescent
if a >= b and a >= c:
    a, b, c = a, b, c
elif b >= a and b >= c:
    a, b, c = b, a, c
else:
    a, b, c = c, a, b

if b < c:
    b, c = c, b


# If logic and print result
if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif a**2 == (b**2) + (c**2):
    print('TRIANGULO RETANGULO')
elif a**2 > (b**2) + (c**2):
    print('TRIANGULO OBTUSANGULO')
elif a**2 < (b**2) + (c**2):
    print('TRIANGULO ACUTANGULO')
if a == b == c:
    print('TRIANGULO EQUILATERO')
elif a == b != c or c == a != b or b == c != a:
    print('TRIANGULO ISOSCELES')

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 23-23 ==============#
# Triangles types
# 18 of March of 2026

# While loop
while 1:
    # Variables declaration
    val1 = int(input('Valor 1:'))
    val2 = int(input('Valor 2:'))

    # If logic and print result
    if val1 < 0 or val1 > 1000 or val2 < 0 or val2 > 1000:
        print('Valor fora do intervalo.\nDigite novamente:')
    elif val1 == val2:
        print('Valor1 == Valor2.\nDigite novamente:')
    elif val1 > val2:
        print('Saída: %d' % (val1 *3))
        break
    else:
        print('Saída: %d' % (val1 *3))
        break

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 24-24 ==============#
# Signal and pair
# 18 of March of 2026

# Variables declaration
a = int(input('Valor: '))

# If logic and print result
if a > 0:
    print('Positivo')
elif a == 0:
    print('Zero')
else:
    print('Negativo')
if a % 2 == 0:
    print('Par')
else:
    print('Impar')

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 25-25 ==============#
# Price discount
# 18 of March of 2026

# Variables declaration
price = float(input('Price: '))

# If logic
if price >= 7000:
    discount = price * 0.25
elif price >= 5000:
    discount = price * 0.15
else:
    discount = price * 0.05

# Print result
print('Valor da compra: %.2f' % (price))
print('Desconto obtido: %.2f' % (discount))
print('Valor da compra com desconto: %.2f' % (price - discount))

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 26-26 ==============#
# Change
# 18 of March of 2026

# Variables declaration
price = float(input('Preço: '))
paid = float(input('Valor pago: '))

# If logic and print result
if price > paid:
    print('Faltando R$: %.2f' % (price - paid))
elif price == paid:
    print('Preço exato')
else:
    print('Troco R$: %.2f' % (price - paid))

#
# ==================== END ====================#
'''


