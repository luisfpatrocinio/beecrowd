def estaDentro(x, y, comprimento, largura):
    step = largura/comprimento
    return y <= step * x

def main():
    comprimento, largura, numSoldados = list(map(int, input().split()))

    time1 = []
    time2 = []

    for i in range(numSoldados):
        x, y, s = list(map(int, input().split()))

        if not estaDentro(x, y, comprimento, largura):
            time1.append(s)
        else:
            time2.append(s)

    somatime1 = 0
    for i in time1:
        somatime1 += i

    somatime2 = 0
    for i in time2:
        somatime2 += i

    print(f"{somatime1} {somatime2}")

main()