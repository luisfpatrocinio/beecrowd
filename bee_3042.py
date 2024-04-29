# TIME LIMIT

def main():
    distancia = int(input())
    trajeto = []
    while distancia != 0:
        trajeto.clear()
        for i in range(distancia):
            pedaco = list(map(int, input().split()))
            trajeto.append(pedaco)

        toques = 0
        linhaAtual = 0
        colunaAtual = 1

        while linhaAtual < distancia - 1:
            print(f"Pedaco {linhaAtual}/{distancia - 1}")
            if trajeto[linhaAtual + 1][colunaAtual] != 0:
                velhaColuna = colunaAtual
                colunaAtual = trajeto[linhaAtual + 1].index(0)
                toquesAdd = abs(colunaAtual - velhaColuna)
                toques += toquesAdd
                print(f"Saí da {velhaColuna} para a {colunaAtual} apertando {toquesAdd} vezes.")
            linhaAtual += 1

        print(toques)

        distancia = int(input())
        
main()