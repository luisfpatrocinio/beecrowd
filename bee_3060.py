def main():
    valorDaCompra = int(input())
    numParcelas = int(input())

    resto = valorDaCompra % numParcelas

    for i in range(numParcelas):
        thisResto = int(resto > 0)
        print(int(valorDaCompra / numParcelas) + thisResto)
        resto -= 1

main()