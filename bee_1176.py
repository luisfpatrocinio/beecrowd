def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def main():
    T = int(input().strip())
    casos = [int(input().strip()) for _ in range(T)]
    for N in casos:
        print(f"Fib({N}) = {fibonacci(N)}")

main()
