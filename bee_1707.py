def main():
    while True:
        try:
            num1, num2 = list(map(int, input().split()))

            somaTotal = 0

            # Obter impares
            minimo = min(num1, num2)
            if minimo % 2 == 0:
                minimo += 1

            # Percorrer intervalo
            for n in range(minimo, max(num1, num2) + 1, 2):
                print(f"Caminho: {n}")
                # impares += str(n)
                caracteres = str(n)
                for char in caracteres:
                    print(f"Somando: +{char}")
                    somaTotal += int(char)
            
            # total = 0
            # for char in impares:
            #     total += int(char)
            
            print(somaTotal)


        except EOFError:
            break

main()