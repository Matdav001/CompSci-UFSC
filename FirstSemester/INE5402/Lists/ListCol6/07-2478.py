participants = dict()

n = int(input())
for _ in range(n):
    data = input().split()
    participants[data[0]] = [data[1], data[2], data[3]]

while True:
    parts = input().split()
    name, gift = parts[0], parts[1]

    if name in participants and gift in participants[name]:
        print("Uhul! Seu amigo secreto vai adorar o/")
    else:
        print("Tente Novamente!")
