def main():
    while True:
        notas = []
        while len(notas) < 2:
            nota = float(input())
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print('nota invalida')
        print(f'media = {(notas[0] + notas[1])/2:.2f}')
        while True:
            print('novo calculo (1-sim 2-nao)')
            x = int(input())
            if x == 1 or x == 2:
                break
        if x == 2:
            break

main()