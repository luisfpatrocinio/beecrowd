def main():
    while True:
        x1, y1, x2, y2 = list(map(int, input().split()))
        if [x1, y1, x2, y2] == [0, 0, 0, 0]:
            return
        
        if x1 == x2 and y1 == y2:
            print(0)
            continue
        
        # Checar diferença
        difx = abs(x2 - x1)
        dify = abs(y2 - y1)

        # Mesma linha ou coluna
        if x1 == x2 or y1 == y2 or difx == dify:
            print(1)
            continue

        print(2)
        continue

main()