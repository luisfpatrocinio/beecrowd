def main():
    n = int(input())
    for i in range(n):
        x, y = list(map(int, input().split()))

        if x > y:
            t = x
            x = y
            y = t

        soma = 0
        for n in range(x+1, y):
            if n % 2 == 1:
                soma += n
        print(soma)

main()