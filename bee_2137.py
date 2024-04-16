def main():
    while True:
        try:
            livros = []
            n = int(input())
            for i in range(n):
                livroParaAdicionar = input()
                livros.append(livroParaAdicionar)
            livros.sort()
            for livro in livros:
                print(livro)
        except EOFError:
            break

main()