def main():
    notas = []
    while len(notas) < 2:
        nota = float(input())
        if nota < 0 or nota > 10:
            print("nota invalida")
            continue
        notas.append(nota)
    
    media = (notas[0] + notas[1]) / 2
    print(f"media = {media}")

main()