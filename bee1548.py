numeroDeCasos = int(input())

naoPrecisaramTrocarPorFila = []

def contarIntactos(array):
    # Fila original:
    filaOriginal = array

    # Array reordenado:
    filaOrdenada = sorted(array, reverse=True)

    # Montamos um array com cada elemento sendo um par entre o original e o novo:
    comparacoes = list(zip(filaOriginal, filaOrdenada))

    # Iterando essa lista, se cada dupla for igual, somamos um
    total = 0
    for i in range(len(comparacoes)):
        par = comparacoes[i]
        if par[0] == par[1]:
            total+=1

    # Retorna o total de alunos intactos
    return total

# Para cada caso:
for n in range(numeroDeCasos):
    numeroDeAlunos = int(input())

    # Obter a quantidade de notas:
    notasDoAluno = list(map(int, input().split(" ")))

    intactosDessaFila = contarIntactos(notasDoAluno)
    # print("Intactos nesta fila: ", intactosDessaFila)
    naoPrecisaramTrocarPorFila.append(intactosDessaFila)

# Printar resultados
for caso in naoPrecisaramTrocarPorFila:
    print(caso)
        
