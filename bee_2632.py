import math

# Magic and Sword
def circuloEncosta(cx, cy, r, x1, x2, y1, y2):
    # print(f"cx: {cx}, cy: {cy}, r: {r}, x1: {x1}, x2: {x2}, y1: {y1}, y2: {y2}")
    return distanciaEntrePontos(x1, y1, cx, cy) <= r or \
           distanciaEntrePontos(x1, y2, cx, cy) <= r or \
           distanciaEntrePontos(x2, y1, cx, cy) <= r or \
           distanciaEntrePontos(x2, y2, cx, cy) <= r

def obterDano(element):
    match element:
        case "fire": return 200
        case "water": return 300
        case "earth": return 400
        case "air": return 100

def distanciaEntrePontos(x1, y1, x2, y2):
    _x1 = float(x1)
    _x2 = float(x2)
    _y1 = float(y1)
    _y2 = float(y2)
    return math.sqrt((_x2 - _x1) ** 2 + (_y2 - _y1) ** 2)

def obterRaioDaMagia(element: str, level: str):
    _level = int(level)
    match element:
        case "fire":
            match _level:
                case 1:
                    return 20
                case 2:
                    return 30
                case 3:
                    return 50
        case "water":
            match _level:
                case 1:
                    return 10
                case 2:
                    return 25
                case 3:
                    return 40
        case "earth":
            match _level:
                case 1:
                    return 25
                case 2:
                    return 55
                case 3:
                    return 70
        case "air":
            match _level:
                case 1:
                    return 18
                case 2:
                    return 38
                case 3:
                    return 60
    return 100
                

def main():
    numTestes = int(input())
    for i in range(numTestes):
        width, height, x1, y1 = list(map(int, input().split()))
        element, level, cx, cy = list(input().split())

        raio = obterRaioDaMagia(element, level)

        # Obter coordenadas
        x2 = x1 + width
        y2 = y1 + height

        # Verificar se a circunferência encosta no retângulo
        if circuloEncosta(cx, cy, raio, x1, x2, y1, y2):
            damage = obterDano(element)
            print(damage)
        else:
            print(0)

main()