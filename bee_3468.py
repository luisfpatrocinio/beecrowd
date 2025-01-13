def main():
    entrada = input().lower()
    
    palavras = {
        "oposicao": "mas",
        "contrariedade": "mas",
        "quantidade": "mais",
        "intensidade": "mais"
    }
    
    print(palavras[entrada])
    

main()