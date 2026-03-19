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
