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
