def main():
    while True:
        numNetos = int(input())
        if numNetos == 0:
            break
        
        presentes = list(map(int, input().split()))
        presentes.sort()

        somas = []

        # print("Presentes: ", presentes)
        for i in range(int(len(presentes) / 2)):
            # print(f"Conferindo presente de numero {i}.")
            ultimoIndice = len(presentes) - 1 - i
            # print(f"Ultimo indice: {ultimoIndice}")
            valor = presentes[i] + presentes[ultimoIndice]
            somas.append(valor)

        maiorSoma = max(somas)
        menorSoma = min(somas)

        print(f"{maiorSoma} {menorSoma}")
        
main()