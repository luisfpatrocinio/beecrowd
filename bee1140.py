frase = input()

while frase != "*":
    frase = frase.lower()
    palavras = frase.split(" ")
    letra = palavras[0][0]

    # será valido até que se prove o contrário
    valido = True
    for palavra in palavras:
        if palavra[0] != letra:
            valido = False
            break
    if valido:
        print("Y")
    else:
        print("N")

    # receber a próxima frase
    frase = input()