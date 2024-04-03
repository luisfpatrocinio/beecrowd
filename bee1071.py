X = int(input())
Y = int(input())

soma = 0

# Troca de lugar se o primeiro for maior.
if X > Y:
    X, Y = Y, X

for num in range(X + 1, Y):
    # Se for impar
    if num % 2 != 0:
        soma += num

print(soma)