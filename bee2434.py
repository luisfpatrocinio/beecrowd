def main():
    n, s = list(map(int, input().split()))
    menorValor = s
    for i in range(n):
        add = int(input())
        s += add
        if s < menorValor:
            menorValor = s

    print(menorValor)

main()