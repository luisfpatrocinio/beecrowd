def main():
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            h = list(map(int, input().split()))
            picos = 0
            for i in range(n):
                if i == 0:
                    if h[i] > h[-1] and h[i] > h[i+1]:
                        picos += 1
                    elif h[i] < h[-1] and h[i] < h[i+1]:
                        picos += 1
                elif i == n-1:
                    if h[i] > h[i-1] and h[i] > h[0]:
                        picos += 1
                    elif h[i] < h[i-1] and h[i] < h[0]:
                        picos += 1
                else:
                    if h[i] > h[i-1] and h[i] > h[i+1]:
                        picos += 1
                    elif h[i] < h[i-1] and h[i] < h[i+1]:
                        picos += 1
            print(picos)

main()