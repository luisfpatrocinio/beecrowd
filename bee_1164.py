def main():
    n = int(input())
    for i in range(n):
        x = int(input())
        if eh_perfeito(x):
            print(f'{x} eh perfeito')
        else:
            print(f'{x} nao eh perfeito')

def eh_perfeito(x):
    soma = 0
    for i in range(1, x):
        if x % i == 0:
            soma += i
    return soma == x

main()