# Brazilian economy
# 11 of may of 2026

# Variables declaration
q = int(input("Digite Q: "))
vec = list(map(int, input("Digite V: ").split()))
s = 0

# Logic loop
for i in range(q):
    s += vec[i]

# Print result
print("N" if s >= q / 2 else "Y")
