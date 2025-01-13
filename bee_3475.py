def main(): 
    numeros = {
        1: "um",
        2: "dois",
        3: "tres",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
        0: "zero"
    }
    entrada = input()

    if len(entrada) <= 1:
        entrada = int(entrada)    
        print(numeros[entrada])
    else:
        for key, value in numeros.items():
            if value == entrada:
                print(key)
                break

main()