def main():
    tipoDeCha = int(input())
    a, b, c, d, e = list(map(int, input().split()))

    corretos = 0
    if a == tipoDeCha: corretos += 1
    if b == tipoDeCha: corretos += 1
    if c == tipoDeCha: corretos += 1
    if d == tipoDeCha: corretos += 1
    if e == tipoDeCha: corretos += 1

    print(corretos)
    pass

main()