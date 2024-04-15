def main():
    k = int(input())

    tops = [1, 3, 5, 10, 25, 50, 100]
    for i in tops:
        if k <= i:
            print(f"Top {i}")
            break

main()