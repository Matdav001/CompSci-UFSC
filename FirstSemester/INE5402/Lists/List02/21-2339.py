# Paper planes
# 18 of March of 2026

# Variables declaration
c, p, f = input('Alunos, folhas a folhas por aluno: ').split()

c = int(c)
p = int(p)
f = int(f)

# If logic and print result
if f * c <= p:
    print('S')
else:
    print('N')