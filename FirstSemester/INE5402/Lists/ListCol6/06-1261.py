while True:
    line = input().split()
    m, n = int(line[0]), int(line[1])

    hay_points = {}
    for _ in range(m):
        entry = input().split()
        word = entry[0]
        value = int(entry[1])
        hay_points[word] = value

    for _ in range(n):
        total_salary = 0

        while True:
            description_line = input().split()

            if description_line == ["."]:
                break

            for word in description_line:
                if word in hay_points:
                    total_salary += hay_points[word]

        print(total_salary)
