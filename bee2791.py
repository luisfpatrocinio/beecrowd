def main():
    c = list(map(int, input().split()))
    indiceEncontrado = 0
    while c[indiceEncontrado] == 0:
        indiceEncontrado += 1

    print(indiceEncontrado + 1)

main()