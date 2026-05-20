while True:
    n = int(input())

    counts = {"EPR": 0, "EHD": 0, "INTRUSOS": 0}

    for _ in range(n):
        student_data = input().split()
        course = student_data[1]

        if course == "EPR":
            counts["EPR"] += 1
        elif course == "EHD":
            counts["EHD"] += 1
        else:
            counts["INTRUSOS"] += 1

    print(f"EPR: {counts['EPR']}")
    print(f"EHD: {counts['EHD']}")
    print(f"INTRUSOS: {counts['INTRUSOS']}")
