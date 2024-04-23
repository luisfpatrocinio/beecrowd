def obterSeculo(ano):
    return int((ano - 1) / 100) + 1

def main():
    while True:
        try:
            ano = int(input())
            print(obterSeculo(ano))
        except EOFError:
            break

main()