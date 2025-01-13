def main():
    dias, pessoas = list(map(int, input().split()))

    n = dias - 1
    chance = n / dias
    while n <= dias - pessoas + 1:
        n -= 1
        chance *= n / dias

    print(chance)

main()