produtos = {
    "Alcool": 0,
    "Gasolina": 0,
    "Diesel": 0
}

valor = int(input())
while valor != 4:
    if valor == 1:
        produtos["Alcool"] += 1
    if valor == 2:
        produtos["Gasolina"] += 1
    if valor == 3:
        produtos["Diesel"] += 1
    valor = int(input())

print(f"MUITO OBRIGADO\nAlcool: {produtos['Alcool']}\nGasolina: {produtos['Gasolina']}\nDiesel: {produtos['Diesel']}")