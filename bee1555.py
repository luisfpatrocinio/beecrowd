# Rafael
def func_r(x, y):
    return (3 * x) ** 2 + y ** 2
    
# Beto
def func_b(x, y):
    return 2 * x ** 2 + (5 * y) ** 2
    
# Carlos
def func_c(x, y):
    return -100 * x + y ** 3

# Número de casos de teste
n = int(input())

for i in range(n):
    # Valores de teste
    x, y = map(int, input().split(" "))

    # Resultados
    r = func_r(x, y)
    b = func_b(x, y)
    c = func_c(x, y)

    # Printar resultados
    if r > b and r > c:
        print("Rafael ganhou")
    elif b > r and b > c:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")
