N = int(input())

pares = []
impares = []

for _ in range(N):
    number = int(input())
    if number % 2 == 0:
        pares.append(number)
    else:
        impares.append(number)

pares.sort()
impares.sort(reverse=True)

for number in pares:
    print(number)

for number in impares:
    print(number)
