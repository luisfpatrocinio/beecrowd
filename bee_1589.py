# Bob Conduite

def main():
    numTestes = int(input())
    for i in range(numTestes):
        r1, r2 = list(map(int, input().split()))
        print(int((r1 + r1 + r2 + r2)/2))

main()