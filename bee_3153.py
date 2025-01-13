def main():
    n = int(input())
    textos = []
    for _ in range(n):
        texto = input()
        if texto.startswith("add"):
            textos.append(str(texto[3:]).strip())
        elif texto.startswith("find"):
            palavra = (texto[4:].strip())
            encontrados = 0
            for i in range(len(textos)):
                esteTexto: str = textos[i]
                encontrados += esteTexto.count(palavra)
            print(encontrados)

main()