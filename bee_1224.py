# https://judge.beecrowd.com/pt/problems/view/1224

def main():
    qntNum = int(input())
    numeros = list(map(int, input().split()))
    
    turno = 1
    while turno < qntNum:
        dupla = [numeros[0], numeros[-1]]
        if turno % 2 == 0:
            # Alberto
            # Confere se a dupla contém o maior elemento de numeros
            if max(numeros) in dupla:
                if numeros[-1] > numeros[0]:
                    print("Último elemento removido.")
                    del(numeros[-1])
                else:
                    print("Primeiro elemento removido.")
                    del(numeros[0])
            else:
                # O maior elemento não está na beirada, então devo pegar q
        else:
            # Wanderley
        turno += 1


main()