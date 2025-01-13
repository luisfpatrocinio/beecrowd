def main():
    numTestes = int(input())
    for i in range(numTestes):
        pa, pb, g1, g2 = input().split()
        pa = int(pa)
        pb = int(pb)
        g1 = float(g1)
        g2 = float(g2)

        tempo = 0
        estouro = False

        while pa <= pb:
            pa = int(pa + g1 * pa / 100.0)
            pb = int(pb + g2 * pb / 100.0)
            tempo += 1
            # print(f"Ano: {tempo}\tPA: {pa}\tPB: {pb}")

            if tempo > 100:
                print("Mais de 1 seculo.")
                estouro = True
                break

        if not estouro:
            print(f"{tempo} anos.")
        

main()