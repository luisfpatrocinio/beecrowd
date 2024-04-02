# Bee - 1120 - Revisão de Contrato

def main():
    while True:
        entrada = input()
        # O ultimo caso de teste é seguido por uma linha que contém apenas dois zeros separados por espaços em branco.
        if entrada == "0 0":
            break
        else:
            entrada = entrada.split()
            numero = entrada[1]
            digito = entrada[0]
            # Processamento
            numero = numero.replace(digito, "")
            if numero == "":
                numero = 0
            else:
                numero = int(numero)
            # Saída
            print(numero)

main()