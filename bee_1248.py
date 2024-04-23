# Plano de Dieta

def main():
    numCasos = int(input())

    for i in range(numCasos):
        cheated = False
        dieta = input()
        cafe = input()
        almoco = input()
        
        comido = cafe + almoco

        # Se comer algo que nao ta na dieta
        for char in comido:
            if char not in dieta:
                cheated = True
                break

        # Formar janta
        janta = ""
        for char in dieta:
            if char not in comido:
                janta += char
        janta = ''.join(sorted(janta))  # ordem alfabética.
        
        if not cheated:
            print(janta)
        else:
            print("CHEATER")


main()