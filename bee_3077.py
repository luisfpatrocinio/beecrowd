def obterSoma(vetor):
    soma = 0
    for i in vetor:
        soma += i
    return soma

def main():
    numTrabalhadores, numEtapas = list(map(int, input().split()))
    distribuicao = list(map(int, input().split()))
    pequis = [0 for i in range(numTrabalhadores)]

    contador = 0
    maxCounts = int(numEtapas / numTrabalhadores)
    somaPorStep = obterSoma(distribuicao)
    
    while contador < maxCounts:
        for i in range(numTrabalhadores):
            pequis[i] += somaPorStep
        contador += 1
    
    for n in range(numEtapas % numTrabalhadores):
        for i in range(numTrabalhadores):
            pequis[i] += distribuicao[(i - n) % numTrabalhadores]

    print(' '.join(map(str, pequis)))

main()