def main():
    n = int(input())
    anterior = 0
    ultimo = 1
    sequencia = "0 1 "
    for i in range(n - 2):
        numero = ultimo + anterior
        anterior = ultimo
        ultimo = numero
        sequencia += str(numero)
        if i < n -3 :
            sequencia += " "

    print(sequencia)

main()