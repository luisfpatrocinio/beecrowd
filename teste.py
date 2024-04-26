def atualizar(_vetor):
    for i in range(len(_vetor)):
        _vetor[i] *= 2
    return _vetor

def main():
    vetor = [2, 2, 4]
    novoVetor = atualizar(vetor.copy())
    print(vetor)
    print(novoVetor)

main()