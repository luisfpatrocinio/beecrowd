def main():
    numCasos = int(input())
    for i in range(numCasos):
        frase = input().lower()
        letters = dict()

        for char in frase:
            if char.isalpha():
                qnt = letters.get(char, 0)
                letters[char] = qnt + 1
                # print(f"Letra adicionada: {char} ({qnt + 1})")
        
        # print(f"Letras: {letters}")
        
        # Obter caracteres que mais se repetem
        mostKey = max(letters, key=lambda k: letters[k])
        # print(f"Letra que mais se repete {mostKey}")

        repeated_letters = [char for char, count in letters.items() if count == letters[mostKey]]
        # print(f"Letras repetidas: {repeated_letters}")

        retorno = ""
        for i in sorted(repeated_letters):
            retorno += i

        print(retorno)
        




main()
