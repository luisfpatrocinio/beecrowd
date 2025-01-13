# Jogo de Tabuleiro
# TIME LIMIT EXCEEDED

class Ficha:
    capturada = False
    def __init__(self, x, y, valor):
        self.x = x
        self.y = y
        self.valor = valor

class Jogador:
    def __init__(self, coeficiente_angular, coeficiente_linear):
        self.a = coeficiente_angular
        self.b = coeficiente_linear
        self.minhasFichas = []


def main():
    # Número de fichas: 
    numFichas = int(input("Numero de fichas: "))

    # Definir fichas:
    fichas = []
    for i in range(numFichas):
        # Entrada: coordenadas
        coords = list(map(int, input().split()))
        # Criar ficha e adicionar no array
        fichas.append(Ficha(coords[0], coords[1], i + 1))

    # Definir jogadores:
    numJogadores = int(input("Numero de jogadores: "))
    jogadores = []
    for i in range(numJogadores):
        # Entrada: coeficiente angular e linear
        coefs = list(map(int, input().split()))
        # Cria jogador
        jogador = Jogador(coefs[0], coefs[1])

        # Aqui já podemos processar o jogo na verdade:
        for ficha in fichas:
            if fichaPertence(ficha, jogador):
                # print(f"Jogador {i + 1} capturou a ficha {ficha.valor}")
                jogador.minhasFichas.append(ficha)
                ficha.capturada = True

        jogadores.append(jogador)

    # Saída:
    for esteJogador in jogadores:
        pontos = len(esteJogador.minhasFichas)
        scoreStr = f"{pontos}"
        for i in range(pontos):
            scoreStr += f" {esteJogador.minhasFichas[i].valor}"
        print(scoreStr)

def fichaPertence(ficha: Ficha, jogador: Jogador):
    if ficha.capturada:
        # print(f"A ficha {ficha.valor} já foi capturada.")
        return False
    # Verifica se a ficha está abaixo da reta y = ax + b
    return ficha.y < jogador.a * ficha.x + jogador.b


main()