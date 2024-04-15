## INCOMPLETA

import math


def main():
    while True:
        try:
            numDias = int(input())
            custo = int(input())
            receitaTotal = 0
            receitas = []
            for i in range(numDias):
                receitaDoDia = int(input())
                receitaTotal += receitaDoDia
                # receitas.append(receitaDoDia)
            
            lucro = receitaTotal - numDias * custo
            print(lucro)

        except EOFError:
            break

main()