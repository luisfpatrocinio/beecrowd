def main():
    inside = 0
    outside = 0
    n = int(input())
    for i in range(n):
        x = int(input())
        if x in [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
            inside += 1
        else:
            outside += 1
    print("{} in".format(inside))
    print("{} out".format(outside))

main()