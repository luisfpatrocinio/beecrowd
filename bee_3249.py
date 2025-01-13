# Death Knight Hero
def main():
    qntBatalhas = int(input())
    qntVitorias = 0
    for _ in range(qntBatalhas):
        batalha = input()
        if batalha.find("CD") == -1:
            qntVitorias += 1

    print(qntVitorias)

main()
