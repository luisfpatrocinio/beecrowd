def main():
    op = input()

    matriz = []
    for i in range(12):
        linha = []
        for j in range(12):
            linha.append(float(input()))
        matriz.append(linha)

    soma = 0
    cont = 0
    for i in range(12):
        for j in range(i + 1, 12):
            soma += matriz[i][j]
            cont += 1

    if op == 'S':
        print("{:.1f}".format(soma))
    elif op == 'M':
        print("{:.1f}".format(soma / cont))

main()