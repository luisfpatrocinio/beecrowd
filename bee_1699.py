# Time limit exceeded

def contarDivisores(numero):
    count = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            count += 1
    return count



def main():
    n = int(input())
    while n != 0:
        rotulos = map(int, input().split())

        bolas = []
        for c in rotulos:
            bolas.append(contarDivisores(c))

        total = 0
        for i in range(len(bolas)):
            total += bolas[i]

        nomes = ["Garen", "Annie"]

        print(nomes[total % 2])
        
        n = int(input())

main()