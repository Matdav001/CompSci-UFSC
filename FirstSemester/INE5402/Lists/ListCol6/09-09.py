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
