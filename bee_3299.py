def main():
    n = input()
    masorte = False
    for i in range(len(n)):
        if n[i] == '1':
            # Encontramos o 1, precisamos saber se o próximo é 3:
            if i + 1 < len(n):
                if n[i + 1] == '3':
                    masorte = True
    
    if masorte:
        print("{} es de Mala Suerte".format(n))
    else:
        print("{} NO es de Mala Suerte".format(n))

main()