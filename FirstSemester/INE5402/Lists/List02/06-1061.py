# Event time
# 16 of March of 2026

# Variables declaration
DIA, DIAINIT = (input('Dia de término: ')).split()
HINIT, COMMA0, MINIT, COMMA1, SINIT = input('Hora de começo: ').split()

DIAINIT = int(DIAINIT)
HINIT = int(HINIT)
MINIT = int(MINIT)
SINIT = int(SINIT)

DIA, DIAFIM = (input('Dia de término: ')).split()
HFIM, COMMA0, MFIM, COMMA1, SFIM = input('Hora de término: ').split()

DIAFIM = int(DIAFIM)
HFIM = int(HFIM)
MFIM = int(MFIM)
SFIM = int(SFIM)

# Seconds calculation
SDIFF = SFIM - SINIT

# Minutes calculation
if SDIFF < 0:
    MDIFF = MFIM - MINIT - 1
    SDIFF = 60 + SDIFF
else:
    MDIFF = MFIM - MINIT

# Hours calculation
if MDIFF < 0:
    HDIFF = HFIM - HINIT - 1
    MDIFF = 60 + MDIFF
else:
    HDIFF = HFIM - HINIT

# Days calculation
if HDIFF < 0:
    DIADIFF = DIAFIM - DIAINIT - 1
    HDIFF = 24 + HDIFF
else:
    DIADIFF = DIAFIM - DIAINIT

# Print result 
print(DIADIFF, 'dia(s)')
print(HDIFF, 'hora(s)')
print(MDIFF, 'minuto(s)')
print(SDIFF, 'segundo(s)')
