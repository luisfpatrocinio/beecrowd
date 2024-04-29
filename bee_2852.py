def converterCaractere(char, chave):
    # ascii: a = 97
    if char == " ":
        return " "
    chaveInd = ord(chave) - 97
    charInd = ord(char) - 97
    retorno = chr(((chaveInd + charInd) % 26) + 97)
    print(f"{chave} -> {char}\t= [{retorno}]")
    return retorno

def ehVogal(char):
    return char in ['a', 'e', 'i', 'o', 'u']

def processarFrase(frase, chave):
    novaFrase = ""
    indChave = 0
    proximoCharEhPalavraNova = True
    estouIgnorando = False
    for i in range(len(frase)):
        chaveChar = chave[indChave % len(chave)]
        char = frase[i]
        if proximoCharEhPalavraNova and ehVogal(char):
            estouIgnorando = True
        
        # Conferir se estamos ignorando essa palavra
        if estouIgnorando:
            novaFrase += char
        else:
            novaFrase += converterCaractere(char, chaveChar)

        if frase[i] != " ": 
            indChave += 1
            proximoCharEhPalavraNova = False
        else:
            proximoCharEhPalavraNova = True
            estouIgnorando = False
    return novaFrase

def main():
    chave = input()
    numPalavras = int(input())
    for i in range(numPalavras):
        frase = input()
        # Processar palavra
        print(processarFrase(frase, chave))

main()