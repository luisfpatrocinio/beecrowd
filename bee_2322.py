def main():
    qntPecas = int(input())
    pecas = list(map(int, input().split()))
    pecas.sort()

    pecaAtual = 0
    pecaFaltando = 0
    for i in range(qntPecas - 1):
        # print(f"{i} - Conferindo peça: ", pecas[i])
        if pecas[i] == pecaAtual + 1:
            pass
        else:
            # print("Opa! Falta: ", i + 1)
            pecaFaltando = i + 1
            break
        pecaAtual += 1

    if pecaFaltando == 0:
        pecaFaltando = qntPecas

    print(pecaFaltando)

main()