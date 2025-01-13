def main():
    # Obter valores do dia 1
    dia1 = input().split()[1]
    hora1, min1, seg1 = map(int, input().split(':'))

    # Obter valores do dia 2
    dia2 = input().split()[1]
    hora2, min2, seg2 = map(int, input().split(':'))

    # Obter total de segundos
    total_segundos = (int(dia2) - int(dia1)) * 86400
    total_segundos += (hora2 - hora1) * 3600
    total_segundos += (min2 - min1) * 60
    total_segundos += seg2 - seg1

    dias = total_segundos // 86400
    total_segundos %= 86400
    horas = total_segundos // 3600
    total_segundos %= 3600
    minutos = total_segundos // 60
    total_segundos %= 60
    segundos = total_segundos

    print(f'{dias} dia(s)')
    print(f'{horas} hora(s)')
    print(f'{minutos} minuto(s)')
    print(f'{segundos} segundo(s)')

main()