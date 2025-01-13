# Contadores para múltiplos
multiplos_2 = 0
multiplos_3 = 0
multiplos_4 = 0
multiplos_5 = 0

# Entrada
quantidade = int(input())

# Leitura dos valores e transformação para inteiros
numeros = list(map(int, input().split()))[:quantidade]

# Itera pelos números e conta os múltiplos
for numero in numeros:
    if numero % 2 == 0:
        multiplos_2 += 1
    if numero % 3 == 0:
        multiplos_3 += 1
    if numero % 4 == 0:
        multiplos_4 += 1
    if numero % 5 == 0:
        multiplos_5 += 1

# Saída
print(f'{multiplos_2} Multiplo(s) de 2')
print(f'{multiplos_3} Multiplo(s) de 3')
print(f'{multiplos_4} Multiplo(s) de 4')
print(f'{multiplos_5} Multiplo(s) de 5')