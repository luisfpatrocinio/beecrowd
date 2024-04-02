def main():
    i = 1
    j = 7

    while i <= 9:
        for _ in range(3):
            print("I={} J={}".format(i, j))
            j -= 1
        i += 2

        # j volta a ser 7
        j = 7

main()