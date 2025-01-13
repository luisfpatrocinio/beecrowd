def main():
    n = int(input())
    cobaias = {'C': 0, 'R': 0, 'S': 0}
    total = 0
    for i in range(n):
        qtd, tipo = input().split()
        cobaias[tipo] += int(qtd)
        total += int(qtd)
    printResults(cobaias, total)

def printResults(cobaias, total):
    print(f'Total: {total} cobaias')
    print(f'Total de coelhos: {cobaias["C"]}')
    print(f'Total de ratos: {cobaias["R"]}')
    print(f'Total de sapos: {cobaias["S"]}')
    print(f'Percentual de coelhos: {cobaias["C"]/total*100:.2f} %')
    print(f'Percentual de ratos: {cobaias["R"]/total*100:.2f} %')
    print(f'Percentual de sapos: {cobaias["S"]/total*100:.2f} %')

main()