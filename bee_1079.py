def calcular_media_ponderada(valores):
    pesos = [2, 3, 5]

    # obter a soma dos valores multiplicados pelos seus pesos
    soma = sum(valores[i] * pesos[i] for i in range(len(pesos)))
    return soma / sum(pesos)

N = int(input())

for _ in range(N):
    valores = list(map(float, input().split()))
    print("{:.1f}".format(calcular_media_ponderada(valores)))
