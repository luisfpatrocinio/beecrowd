def determinar_nivel(velocidade):
    if velocidade >= 20:
        return 3
    elif velocidade >= 10:
        return 2
    else:
        return 1

def main():
    while True:
        try:
            L = int(input().strip())
            velocidades = list(map(int, input().strip().split()))
            max_velocidade = max(velocidades)
            nivel = determinar_nivel(max_velocidade)
            print(nivel)
        except EOFError:
            break

if __name__ == "__main__":
    main()
