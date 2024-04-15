## INCOMPLETO

def operacao(n):
    n = int(n)
    if n % 2 == 0:
        return n / 2
    else:
        return n * 3 + 1

def main():
    n = int(input())
    seq = list(map(int, input().split()))
    operSeq = list(map(operacao, seq))
    x = 0
    y = 0
    

    for numAtual in seq:
        # É engraçado:
        valorOperado = operacao(numAtual)
        if valorOperado in seq:
            y += 1
        # É estranho:
        if numAtual in operSeq:
            x += 1

    print(f"E = {x} || E = {y}")

main()