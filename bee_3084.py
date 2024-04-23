def main():
    while True:
        try:
            h, m = list(map(int, input().split()))

            grausPorHora = int(360 / 12)
            grausPorMinuto = int(360 / 60)

            horaStr = str(int(h / grausPorHora))
            minutoStr = str(int(m / grausPorMinuto))

            if len(horaStr) < 2:
                horaStr = "0" + horaStr
            if len(minutoStr) < 2:
                minutoStr = "0" + minutoStr


            print(horaStr+":" + minutoStr)
        except EOFError:
            break

main()