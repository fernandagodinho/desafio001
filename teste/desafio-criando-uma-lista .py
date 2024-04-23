def gerenciar_equipamentos():
    equipamentos = []

    print("Por favor, insira os detalhes de até três equipamentos:")

    for i in range(3):
        equipamento = input("Insira o nome do equipamento: ")
        equipamentos.append(equipamento)

    print("\nLista de Equipamentos:")
    for equipamento in equipamentos:
        print("- " + equipamento)
        print(f"-{item}")

gerenciar_equipamentos()
