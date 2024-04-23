def main():
    numCasos = int(input())
    for i in range(numCasos):
        frase = input()

        letras = []
        # Percorrer letra por letra
        for char in frase:
            # é um caractere normal?
            if not char.isalpha():
                continue    # pular pra proxima letra caso nao seja uma letra

            # perguntar se o caractere ja foi separadinho
            if char not in letras:
                letras.append(char)
            
        # checar o tamanho do vetor
        tamanho = len(letras)

        if tamanho >= 26:
            print("frase completa")
        elif tamanho >= 13:
            print("frase quase completa")
        else:
            print("frase mal elaborada")


main()