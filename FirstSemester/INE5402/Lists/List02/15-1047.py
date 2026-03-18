# Game time with minutes
# 18 of March of 2026

# Variables declaration
hinit, minit, hfim, mfim = input('Horario inicial e final: ').split()

hinit = int(hinit)
minit = int(minit)
hfim = int(hfim)
mfim = int(mfim)

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