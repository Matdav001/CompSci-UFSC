n = int(input())

greetings = {}

for _ in range(n):
    lang = input()
    greeting = input()
    greetings[lang] = greeting

# Read the number of children
m = int(input())

# Process each child
for _ in range(m):
    name = input()
    language = input().strip()

    # Print the label as required
    print(name)
    print(greetings[language])
    print()
