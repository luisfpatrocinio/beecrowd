def main():
    while True:
        numTestes = int(input())
        if numTestes == 0:
            break
        pontos = [0, 0]
        while numTestes > 0:
            m, n = list(map(int, input().split()))
            if m > n:
                pontos[0] += 1
            elif n > m:
                pontos[1] += 1
            numTestes -= 1
            if numTestes == 0:
                print(f"{pontos[0]} {pontos[1]}")

        

main() 