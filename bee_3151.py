# UOJ_3151

def main():
    while True:
        try: 
            numTestes = int(input())
            for n in range(numTestes):
                numIogurtes, capacidadeGarrafa = list(map(int, input().split()))
                valores = []
                volumes = []
                gostPorLitro = []
                for i in range(numIogurtes):
                    inputSecond = input().split()
                    valorIog, volumeIog = [0, 0]
                    if len(inputSecond) >= 2:
                        valorIog = float(inputSecond[0])
                        volumeIog = float(inputSecond[1])
                    else:
                        continue
                    
                    valores.append(valorIog)
                    volumes.append(volumeIog)
                    gostosura = float(valorIog/volumeIog)
                    gostPorLitro.append(gostosura)
                    # print(f"O iogurte {i} tem g/l {gostosura}")

                # Processamento
                # Enquanto couber iogurte, vai botando paizao
                gostosuraAtual = 0
                volumeAtual = 0
                while volumeAtual < capacidadeGarrafa and len(volumes) > 0:
                    # Colocar primeiro o iogurte de maior valor.
                    # Encontrar o iogurte mais saboroso:
                    # print(f"Ciclo: temos as gostosuras:\t{gostPorLitro}")
                    valorDaMaiorGostPorLitro = max(gostPorLitro)
                    indDesejado = gostPorLitro.index(valorDaMaiorGostPorLitro)
                    while volumes[indDesejado] > 0:
                        volumeAtual += 1
                        volumes[indDesejado] -= 1
                        gostosuraAtual += gostPorLitro[indDesejado]
                    del volumes[indDesejado]
                    del valores[indDesejado]
                    del gostPorLitro[indDesejado]
                    
                # Mostrar total de gostosura
                print(f"{gostosuraAtual:.2f}")
        except EOFError:
            break

main()