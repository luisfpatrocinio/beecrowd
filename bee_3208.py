def main():
    numTests = 20
    for i in range(numTests):
        inputs = list(map(int, input().split()))

        if len(inputs) <= 1:
            continue

        chave, tamMin = inputs[0], inputs[1]

        if chave == 0 and tamMin == 0:
            break

        analise = analisarChave(chave, tamMin)
        if analise == 0:
            print("GOOD")
        else:
            print(f"BAD {analise}")
        
# Retorna true se a chave os fatores forem maiores que o minimo
def analisarChave(chave, tamMin):
    fatores = obterFatores(chave)
    # print("os fatores são: ", fatores)
    for fator in fatores:
        if fator == 1:
            continue

        if fator >= tamMin:
            return 0
        else:
            return fator
    

def obterFatores(chave):
    fatores = []
    limite = int(chave ** 0.5) + 1
    for i in range(2, limite):
        if chave % i == 0:
            fatores.append(i)
            if i != chave // i:
                fatores.append(chave // i)
    return fatores

main()