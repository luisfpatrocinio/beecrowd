import math

def calculaKBJs(n):
    return int(math.log2(n))

def main():
    while True:
        try:
            n = int(input())
            if n == 1:
                print(0)
                continue
            print(calculaKBJs(n))
        except EOFError:
            break

main()