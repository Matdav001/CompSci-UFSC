# Area Code
# 16 of March of 2026

# Variables declaration
CODE = int(input('DDD: '))

# If logic and print result 
match CODE: 
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