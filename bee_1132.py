def main():
    numero1 = int(input())
    numero2 = int(input())
    soma = 0

    if numero1 > numero2:
        numero1, numero2 = numero2, numero1

    for i in range(numero1, numero2 + 1):
        if i % 13 != 0:
            soma += i

    print(soma)

    
main()