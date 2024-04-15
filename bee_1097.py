def main():
    i = -1
    j = 7
    n = 0
    m = 0
    while n < 5:
        i += 2
        j += 2
        n += 1
        m = 0
        while m < 3:
            m += 1
            print(f"I={i} J={j - m - 1}")

main()