def main():
    numCasos = int(input())
    for i in range(numCasos):
        a, b = list(map(int, input().split()))
        saida = "encaixa" if encaixa(a, b) else "nao encaixa"
        print(saida)

def encaixa(a: int, b: int):
    if b > a:
        return False
    
    while b > 0:
        # Compara o último dígito de A com o de B
        if a % 10 != b % 10:
            return False
        
        # Retira o último dígito
        a = a // 10
        b = b // 10
    
    # Se chegou até aqui é porque tá tudo certo
    return True



main()