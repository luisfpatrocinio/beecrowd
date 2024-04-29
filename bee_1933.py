def main():
    a, b = list(map(int, input().split()))

    if a == b:
        # é bom ter um trio agora
        c = a
    else:
        c = max(a, b)
    
    print(c)

main()