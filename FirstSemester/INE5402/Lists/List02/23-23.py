# Triangles types
# 18 of March of 2026

# While loop
while 1:
    # Variables declaration
    a = int(input('Valor 1:'))
    b = int(input('Valor 2:'))

    # If logic and print result
    if a < 0 or a > 1000 or b < 0 or b > 1000:
        print('Valor fora do intervalo.\nDigite novamente:')
    elif a == b:
        print('Valor1 == Valor2.\nDigite novamente:')
    elif a > b:
        print('Saída: %d' % (a *3))
        break
    else:
        print('Saída: %d' % (b *3))
        break