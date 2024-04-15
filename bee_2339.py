def main():
    c, p, f = list(map(int, input().split()))
    
    if p / c >= f:
        print("S")
    else:
        print("N")


main()