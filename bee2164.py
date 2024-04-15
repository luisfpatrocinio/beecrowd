import math

def binet(n):
    a = math.pow(((1 + math.sqrt(5)) / 2), n)
    b = math.pow(((1 - math.sqrt(5)) / 2), n)
    return (a - b) / math.sqrt(5)

def main():
    n = int(input())
    binet_value = binet(n)
    # Printar com uma casa decimal.
    print(f"{binet_value:.1f}")

main()