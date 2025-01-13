def soma_pares_consecutivos(x):
    if x % 2 != 0:
        x += 1  # Ajusta para o próximo número par se x for ímpar
    soma = 0
    for _ in range(5):
        soma += x
        x += 2  # Avança para o próximo número par
    return soma

def main():
    while True:
        x = int(input().strip())
        if x == 0:
            break
        print(soma_pares_consecutivos(x))

main()
