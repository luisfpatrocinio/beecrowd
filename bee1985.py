precos = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}

n = int(input())

valorTotal = 0

for _ in range(n):
    linha = input().split()
    produto = int(linha[0])
    quantidade = int(linha[1])

    precoDaCompra = precos[produto] * quantidade

    valorTotal += precoDaCompra

print(f'{valorTotal:.2f}')
