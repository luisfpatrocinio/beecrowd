def main():
    numero = int(input())
    brancas = numero ** 2 // 2 + int(numero % 2 != 0)
    pretas = numero ** 2 // 2
    print(f"{brancas} casas brancas e {pretas} casas pretas")

main()