def construir_matriz(N):
    matriz = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matriz[i][j] = min(i, j, N-i-1, N-j-1) + 1
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{x:>3}" for x in linha))
    print()

def main():
    while True:
        N = int(input())
        if N == 0:
            break
        matriz = construir_matriz(N)
        imprimir_matriz(matriz)

if __name__ == "__main__":
    main()