def main():
    quantidade = int(input())
    pomekons = []
    for i in range(quantidade):
        nomeDoPomekon = input()
        if nomeDoPomekon not in pomekons:
            pomekons.append(nomeDoPomekon)
    print('Falta(m) {} pomekon(s).'.format(151 - len(pomekons)))
    
main()