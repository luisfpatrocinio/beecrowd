def main():
    numAlunos, indPremiado = list(map(int, input().split()))
    nomesAlunos = []
    for i in range(numAlunos):
        nomesAlunos.append(input())

    nomesAlunos.sort()
    print(nomesAlunos[indPremiado - 1])

main()