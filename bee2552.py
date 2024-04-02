
def main():
    while True:
        try:
            # Entrada:
            # Obter tamanho do tabuleiro
            setupTabuleiro = input().split()
            N = int(setupTabuleiro[0])
            M = int(setupTabuleiro[1])

            # Obter linhas do tabuleiro
            tabuleiro = []
            for _ in range(N):
                tabuleiro.append(map(int, input().split()))

        except EOFError:
            break
    
main()