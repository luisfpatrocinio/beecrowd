# https://judge.beecrowd.com/pt/problems/view/3170

import math

def main():
    qntBolinhas = int(input())
    qntGalhos = int(input())

    bolasPrecisa = math.floor(qntGalhos / 2)
    bolasFaltam = bolasPrecisa - qntBolinhas

    if bolasFaltam > 0:
        print(f"Faltam {bolasFaltam} bolinha(s)")
    else:
        print(f"Amelia tem todas bolinhas!")

main()