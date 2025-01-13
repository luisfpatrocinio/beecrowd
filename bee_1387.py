def main():
    # Inicializar
    left = -1
    right = -1
    
    # Processar
    while left != 0 and right != 0:
        left, right = list(map(int, input().split()))
        
        # Saída
        if left != 0 and right != 0:
            print(left + right)
main()