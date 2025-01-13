def main():
    numDivisoes = int(input())
    divisoes = list(map(int, input().split()))
    
    resultado = 0
    for i in range(len(divisoes)):
        resultado += divisoes[i]
    
    resultado -= len(divisoes)

    print(resultado)

main()