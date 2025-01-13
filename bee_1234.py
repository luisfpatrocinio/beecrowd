def main():
    while True:
        try:
            sentenca = input()
            estado = 1 # 0 - maiusculo, 1 - minusculo
            novaSentenca = ""
            for char in sentenca:
                if ehEspaco(char):
                    novaSentenca += char
                    continue
                novaSentenca += obterLetraMaiuscula(char) if estado == 1 else tornarMinusculo(obterLetraMaiuscula(char))
                estado += 1
                estado = estado % 2
            
            print(novaSentenca)
        except EOFError:
            break

def ehMaiusculo(c: str) -> bool:
    return ord(c) >= 65 and ord(c) <= 90

def ehMinusculo(c: str) -> bool:
    return ord(c) >= 97 and ord(c) <= 122

def tornarMaiusculo(c: str) -> str:
    return chr(ord(c) - 32)

def tornarMinusculo(c: str) -> str:
    return chr(ord(c) + 32)

def obterLetraMaiuscula(c: str) -> str:
    # se ja for maiuscula, retornar
    if ehMaiusculo(c):
        return c
    return tornarMaiusculo(c)

def ehEspaco(c: str) -> bool:
    return ord(c) == 32

main()