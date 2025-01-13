def imprimir_vetor(tipo, vetor):
    for i, valor in enumerate(vetor):
        print(f"{tipo}[{i}] = {valor}")

def main():
    pares = []
    impares = []

    for _ in range(15):
        x = int(input().strip())
        
        if x % 2 == 0:
            pares.append(x)
            if len(pares) == 5:
                imprimir_vetor("par", pares)
                pares = []
        else:
            impares.append(x)
            if len(impares) == 5:
                imprimir_vetor("impar", impares)
                impares = []

    # Imprimir o restante dos vetores
    if impares:
        imprimir_vetor("impar", impares)
    if pares:
        imprimir_vetor("par", pares)

main()
