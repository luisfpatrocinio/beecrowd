# 2416 - Corrida
def main():
    distancia, comprimento = list(map(int, input().split()))
    print(distancia % comprimento)

main()