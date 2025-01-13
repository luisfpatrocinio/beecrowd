def main():
    numCasos = int(input())

    battle = {
        "tesoura": ["papel", "lagarto"],
        "papel": ["pedra", "Spock"],
        "pedra": ["lagarto", "tesoura"],
        "lagarto": ["Spock", "papel"],
        "Spock": ["tesoura", "pedra"],
    }

    for i in range(numCasos):
        escolhas = input().split()

        if escolhas[0] == escolhas[1]:
            # Empate
            resultado = "De novo!"
        elif escolhas[1] in battle[escolhas[0]]:
            resultado = "Bazinga!"
        else:
            resultado = "Raj trapaceou!"

        print(f"Caso #{i+1}: {resultado}")


main()