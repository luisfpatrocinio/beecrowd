import math
def main():
    numPorLinha, fim = list(map(int, input().split()))
    
    num = 1
    for i in range(math.floor(fim / numPorLinha)):
        texto = ""
        for t in range(numPorLinha):
            texto += str(num)
            if i < numPorLinha - 1:
                texto += " "
            
            num += 1
        print(texto)

main()