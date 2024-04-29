def trocarLetraPorNumero(char: str) -> int:

    if char == " ":
        return "0"

    asciiCode = ord(char)
   # print(f"A letra {char} virou asciiCode {asciiCode} inicialmente.")
    asciiCode -= 65
   # print(f"Subtraindo 65 ficou {asciiCode}.")
    

    retorno = ""

    # Caso seja maiusculo:
    if asciiCode >= 32:
        asciiCode -= 32
    else:
        retorno += "#"
    # A = 0, B = 1, C = 2
    
    alfabeto    = [2, 2, 2, 3, 3, 3, 
                4, 4, 4, 5, 5, 5, 6, 6, 6,
                7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
    
    reps        = [1, 2, 3, 1, 2, 3,
                1, 2, 3, 1, 2, 3, 1, 2, 3,
                1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4]
    
    # indice 2 = 222
    # indice 5 = F 3x = 333

   # print(f"A letra {char} corresponde ao indice {asciiCode}.")
   # print(f"Precisa ser repetida {reps[asciiCode]}")
    retorno += str(alfabeto[asciiCode]) * reps[asciiCode]

    return retorno

def main():
    # Entrada
    numCasos = int(input())
    for i in range(numCasos):
        frase = input()
    
        resultado = ""
        # Processamento
        for char in frase:
            # A = 65
            # A = 65 + 32 = 97
            digito = trocarLetraPorNumero(char)

            # Conferir se o ultimo digito é igual ao que vai ser inserido
            ultimoDigito = ""
            if len(resultado) > 0:
                ultimoDigito = resultado[len(resultado) - 1]
            if ultimoDigito == digito[0]:
                digito = "*" + digito
            
            resultado += digito

            # ---   222#2-

        # Saída
        print(resultado)

main()