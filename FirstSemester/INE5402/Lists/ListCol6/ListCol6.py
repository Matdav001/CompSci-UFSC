#
#
# ListCol6
#
#

'''
#
# ============= EXERCISE: 01-1281 =============#

n = int(input())

for _ in range(n):
    # Read the number of products available
    m = int(input())
    prices = dict()
    
    # Build the price dictionary
    for _ in range(m):
        line = input().split()
        prices[line[0]] = float(line[1])
        
    # Read the number of items to be bought
    p = int(input())
    total_spent = 0.0
    
    # Calculate the total cost
    for _ in range(p):
        line = input().split()
        product_name = line[0]
        quantity = int(line[1])
        
        
        total_spent += prices[product_name] * quantity
    
    # Output the formatted result
    print(f"R$ {total_spent:.2f}")


#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 02-2482 =============#
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

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 03-1911 =============#
while True:
    n = int(input())
    if n == 0:
        break
        
    students = {}
    for _ in range(n):
        parts = input().split()
        students[parts[0]] = parts[1]
        
    m = int(input())
    
    daily_signatures = {}
    for _ in range(m):
        parts = input().split()
        daily_signatures[parts[0]] = parts[1]
        
    false_count = 0
    
    for name, today_sig in daily_signatures.items():
        original_sig = students[name]
        
        diffs = 0
        len_orig = len(original_sig)
        len_sign = len(today_sig)
        max_len = max(len_orig, len_sign)
        
        for i in range(max_len):
            if i >= len_orig or i >= len_sign or original_sig[i] != today_sig[i]:
                diffs += 1
        
        if diffs > 1:
            false_count += 1
            
    print(false_count)


#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 04-1763 =============#
# Create the dictionary with the provided database
greetings = {
    "brasil": "Feliz Natal!",
    "alemanha": "Frohliche Weihnachten!",
    "austria": "Frohe Weihnacht!",
    "coreia": "Chuk Sung Tan!",
    "espanha": "Feliz Navidad!",
    "grecia": "Kala Christougena!",
    "estados-unidos": "Merry Christmas!",
    "inglaterra": "Merry Christmas!",
    "australia": "Merry Christmas!",
    "portugal": "Feliz Natal!",
    "suecia": "God Jul!",
    "turquia": "Mutlu Noeller",
    "argentina": "Feliz Navidad!",
    "chile": "Feliz Navidad!",
    "mexico": "Feliz Navidad!",
    "antardida": "Merry Christmas!",
    "canada": "Merry Christmas!",
    "irlanda": "Nollaig Shona Dhuit!",
    "belgica": "Zalig Kerstfeest!",
    "italia": "Buon Natale!",
    "libia": "Buon Natale!",
    "siria": "Milad Mubarak!",
    "marrocos": "Milad Mubarak!",
    "japao": "Merii Kurisumasu!",
}

while True:
    country = input()

    if country in greetings:
        print(greetings[country])
    else:
        print("--- NOT FOUND ---")

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 05-1953 =============#
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

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 06-1261 =============#
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

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 07-2478 =============#
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

#
# ==================== END ====================#
'''


'''
#
# ============= EXERCISE: 08-1430 =============#
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

#
# ==================== END ====================#
'''


'''
#
# ============== EXERCISE: 09-09 ==============#
cadastros = []
ano_atual = 2026

while True:
    print("\n--- MENU DE CADASTRO ---")
    print("a - Cadastrar usuário")
    print("b - Imprimir dados (pesquisar pelo nome)")
    print("c - Imprimir dados (todos os usuários)")
    print("d - Encerrar o programa")

    option = input("Escolha uma opção: ").lower()

    if option == "a":
        pessoa = {}
        pessoa["nome"] = input("Nome: ")
        ano_nascimento = int(input("Ano de nascimento: "))
        pessoa["idade"] = ano_atual - ano_nascimento
        pessoa["ctps"] = int(input("Carteira de Trabalho (0 se não tiver): "))

        if pessoa["ctps"] != 0:
            pessoa["ano_contratacao"] = int(input("Ano de contratação: "))
            pessoa["salario"] = float(input("Salário: "))

            anos_trabalhados = ano_atual - pessoa["ano_contratacao"]
            anos_faltando = 35 - anos_trabalhados

            pessoa["idade_aposentadoria"] = pessoa["idade"] + anos_faltando

        cadastros.append(pessoa)
        print("Cadastro realizado com sucesso!")

    elif option == "b":
        nome_busca = input("Digite o nome para pesquisar: ")
        encontrado = False
        for p in cadastros:
            if p["nome"].lower() == nome_busca.lower():
                print("\n--- Dados encontrados ---")
                for chave, valor in p.items():
                    print(f"{chave.capitalize()}: {valor}")
                encontrado = True
        if not encontrado:
            print("Usuário não encontrado.")

    elif option == "c":
        if not cadastros:
            print("Nenhum usuário cadastrado.")
        else:
            print("\n--- Lista de todos os usuários ---")
            for p in cadastros:
                print("-" * 30)
                for chave, valor in p.items():
                    print(f"{chave.capitalize()}: {valor}")

    elif option == "d":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida, tente novamente.")

#
# ==================== END ====================#
'''


