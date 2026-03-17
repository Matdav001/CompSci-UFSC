# Event time
# 16 of March of 2026

# Variables declaration
dia, diainit = (input('Dia de término: ')).split()
hinit, comma0, minit, comma1, sinit = input('Hora de começo: ').split()

diainit = int(diainit)
hinit = int(hinit)
minit = int(minit)
sinit = int(sinit)

dia, diafim = (input('Dia de término: ')).split()
hfim, comma0, mfim, comma1, sfim = input('Hora de término: ').split()

diafim = int(diafim)
hfim = int(hfim)
mfim = int(mfim)
sfim = int(sfim)

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
