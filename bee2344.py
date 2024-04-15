def main():
    nota = int(input())
    conceito = "E"
    if nota > 85: conceito = "A"
    elif nota > 60: conceito = "B"
    elif nota > 35: conceito = "C"
    elif nota > 0: conceito = "D"
    print(conceito)

main()