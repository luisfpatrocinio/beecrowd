import math

def to32(n):
    digitos = []
    resto = n
    while resto >= 32:
        digitos.append(resto % 32)
        resto = math.floor(resto / 32)
    digitos.append(resto)

    # print(f"Digitos antes: {digitos}")
    # for i in range(len(digitos)):
        # digitos[i] = 32 ** i * digitos[i]

    # print(f"Digitos durante: {digitos}")
    digitos = list(map(numeroNaBase32, digitos))
    # print(f"Digitos depois: {digitos}")
    
    result = ""
    for i in range(len(digitos)):
        result += str(digitos[len(digitos) - 1 - i])
    return result

def numeroNaBase32(n):
    if n < 10:
        return str(n)
    else:
        asciiCode = 65 + n - 10
        return chr(asciiCode)

def main():
    while True:
        # Receber numero
        n = int(input())

        # Transformar para base 32
        result = to32(n)

        #Exibir resultado
        print(result)

        if n == 0:
            break

        

main()