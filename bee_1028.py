# Simplesmente obter o MDC entre dois numeros
def main():
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        print(mdc(a, b))

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

main()