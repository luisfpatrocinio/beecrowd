def main():
    p1, c1, p2, c2 = list(map(int, input().split()))
    
    r1 = p1 * c1
    r2 = p2 * c2
    
    if r1 == r2:
        print(0)
    elif r1 < r2:
        print(1)
    elif r2 < r1:
        print(-1)

main()