# Vice champion
# 16 of March of 2026

# Variables declaration
cv, ce, cs, fv, fe, fs = input('Números: ').split()

# Variables conversion
cv = int(cv) 
ce = int(ce) 
cs = int(cs) 
fv = int(fv) 
fe = int(fe)
fs = int(fs) 

# Points calculation
cpoints = cv * 3 + ce
fpoints = fv * 3 + fe

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