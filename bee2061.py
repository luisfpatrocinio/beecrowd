def main():
    n, m = list(map(int, input().split()))

    for i in range(m):
        acao = input()
        if acao == "fechou":
            n -= 1
            n += 2
        elif acao == "clicou":
            n -= 1

    print(n)

main()