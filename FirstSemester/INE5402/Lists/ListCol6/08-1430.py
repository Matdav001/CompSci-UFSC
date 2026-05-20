notes = {"W": 64, "H": 32, "Q": 16, "E": 8, "S": 4, "T": 2, "X": 1}

while True:
    line = input().strip()

    if line == "*":
        break

    measures = line.split("/")

    correct_count = 0

    for measure in measures:
        if not measure:
            continue

        measure_duration = 0
        for note in measure:
            measure_duration += notes[note]

        if measure_duration == 64:
            correct_count += 1

    print(correct_count)
