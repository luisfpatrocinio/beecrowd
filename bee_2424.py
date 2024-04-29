def main():
    x, y, = list(map(int, input().split()))
    dentro = x >= 0 and x <= 432 and y >= 0 and y <= 468
    print("dentro" if dentro else "fora")

main()