def main():
    aposta = list(map(int, input().split()))
    sorteados = list(map(int, input().split()))

    acertos = 0
    for i in range(len(aposta)):
        if aposta[i] in sorteados:
            acertos += 1

    if acertos >= 6:
        print("sena")
    elif acertos >= 5:
        print("quina")
    elif acertos >= 4:
        print("quadra")
    elif acertos >= 3:
        print("terno")
    else:
        print("azar")
        
main()