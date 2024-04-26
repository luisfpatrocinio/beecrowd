# Dança Indígena
from time import sleep


def atualizar(espacos: list):
    espacosAtual = espacos.copy()
    novosEspacos = [0 for _ in espacosAtual]

    for i in range(len(espacos)):
        # Se nao tiver indio aqui, skip
        if espacosAtual[i] == 0:
            # print(f"espaco {i} tem ninguem")
            continue

        # Obter valor do espaco atual
        thisValue = espacosAtual[i]

        # Definir pra onde esse indio vai
        tamanho = len(espacos)
        proxInd = (i + thisValue) % tamanho

        # print(f"Espaco: {i} vai pro: {proxInd}")
        novoValor = thisValue if novosEspacos[proxInd] == 0 else abs(thisValue)
        espacos[proxInd] += novoValor
        novosEspacos[proxInd] += novoValor
        espacos[i] = novosEspacos[i]


def checar(espacos, espacosInicial):
    for i in range(len(espacos)):
        if espacos[i] != espacosInicial[i]:
            return False
    return True

def main():
    # Entrada
    qntToras, qntIndios = list(map(int, input().split()))
    espacos = [0 for i in range(qntToras)]
    for i in range(qntIndios):
        indTora, sentido = list(map(int, input().split()))
        espacos[indTora - 1] = sentido
        print(espacos)
    espacosInicial = espacos.copy()
    
    # Processamento
    # A dança acaba quando o estado das toras volta ao inicial.
    batidas = 0
    while True:
        atualizar(espacos)
        batidas += 1
        print(f"{batidas}\t - {espacos}")
        sleep(0.25)
        

        if checar(espacos, espacosInicial):
            break



    # Saída
    # Exibir a quantidade de batidas de tambor
    # necessárias para que a dança acabe.
    print(f"Batidas: {batidas}")

main()