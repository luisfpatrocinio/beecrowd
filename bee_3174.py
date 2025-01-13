# NAO CONSEGUI
def main():
    # Dicionario com qnt de horas para produzir um presente
    horasPorGrupo = {
        "bonecos": 8,
        "arquitetos": 4,
        "musicos": 6,
        "desenhistas": 12
    }

    qntElfos = int(input())
    
    qntPresentes = 0

    # Processa as informações de cada elfo
    for _ in range(qntElfos):
        elfo, grupo, horas = input().split()
        horas = int(horas)
        
        # Calcula o número de presentes que o elfo pode produzir e acumula no total
        qntPresentes += horas // horasPorGrupo[grupo]

    # Exibe a quantidade total de presentes
    print(qntPresentes)

main()