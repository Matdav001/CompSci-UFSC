# Coast Guard
# 1 of April of 2026

# While loop
while True:
    # Variable declaration
    d, vf, vg = input("Digite D, Vf e Vg: ").split()
    d, vf, vg = int(d), int(vf), int(vg)

    # Max Distance calculation
    hipo = (d**2 + 144) ** 0.5

    # Speed logic
    if vf >= vg:
        print("N")
    # Speed distance logic
    elif (12 / vf) < (hipo / vg):
        print("N")
    else:
        print("S")
