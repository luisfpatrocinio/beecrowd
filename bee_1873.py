def main():
    numCasos = int(input())

    battle = {
        "tesoura": ["papel", "lagarto"],
        "papel": ["pedra", "spock"],
        "pedra": ["lagarto", "tesoura"],
        "lagarto": ["spock", "papel"],
        "spock": ["tesoura", "pedra"],
    }

    for i in range(numCasos):
        escolhas = input().split()

        if escolhas[0] == escolhas[1]:
            # Empate
            resultado = "empate"
        elif escolhas[1] in battle[escolhas[0]]:
            resultado = "rajesh"
        else:
            resultado = "sheldon"

        print(resultado)


main()