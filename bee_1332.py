def valorNumerico(palavra):
    if len(palavra) >= 5:
        return 3

    oneAcertos = 0

    for i in range(len(palavra)):
        char = palavra[i]
        if char == 'o' and i == 0:
            oneAcertos += 1
        if char == 'n' and i == 1:
            oneAcertos += 1
        if char == 'e' and i == 2:
            oneAcertos += 1

    if oneAcertos >= 2:
        return 1
    
    return 2
        


def main():
    numCasos = int(input())
    for i in range(numCasos):
        palavra = input()
        print(valorNumerico(palavra))

main()