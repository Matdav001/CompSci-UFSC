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
