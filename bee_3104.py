def main():
    a = int(input())
    b = int(input())

    while a > b:
        a -= b
    
    print(a % b)

main()  