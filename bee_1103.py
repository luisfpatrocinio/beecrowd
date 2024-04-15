def main():
    while True:
        h1, m1, h2, m2 = list(map(int, input().split()))

        # Encerrar programa:
        if (h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0):
            break

        minutos1 = h1 * 60 + m1
        minutos2 = h2 * 60 + m2

        if minutos2 >= minutos1:
            minutos = minutos2 - minutos1

        else:
            minutos = 24 * 60 - minutos1 + minutos2
        
        print(minutos)

main()