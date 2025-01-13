def main():
    numCasos = int(input())
    for _ in range(numCasos):
        entrada = input()
        digito1 = int(entrada[0])
        digito2 = int(entrada[2])
        if digito1 == digito2:
            print(digito1 * digito2)
        elif 'A' <= entrada[1] <= 'Z':
            print(digito2 - digito1)
        else:
            print(digito2 + digito1)
    pass

main()

