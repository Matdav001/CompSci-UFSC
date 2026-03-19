# New die
# 18 of March of 2026
# Do not consider the number of cases

# Variables declaration
d1 = int(input())
d2, d3, d4, d5 = input().split()
d6 = int(input())

# Variables conversion
d2, d3, d4, d5 = int(d2), int(d3), int(d4), int(d5)

# If logic and print result
if d1 + d6 != 7:
    print('NAO')
elif d2 + d4 != 7:
    print('NAO')
elif d3 + d5 != 7:
    print('NAO')
else:
    print('SIM')
