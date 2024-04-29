def min_meias_para_par(N):
    # Se Rangel tem apenas um par de meias de cada cor, ele precisa de pelo menos N + 1 meias para formar um par
    return N + 1

# Leitura da entrada
N = int(input())

# Chamada da função para calcular a quantidade mínima de meias necessárias
resultado = min_meias_para_par(N)

# Impressão do resultado
print(resultado)