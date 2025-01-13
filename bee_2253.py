def temMaiuscula(senha: str):
    for char in senha:
        if ord("A") <= ord(char) <= ord("Z"):
            return True
    return False

def temMinuscula(senha: str):
    for char in senha:
        if ord("a") <= ord(char) <= ord("z"):
            return True
    return False

def temNumero(senha: str):
    for char in senha:
        if ord("0") <= ord(char) <= ord("9"):
            return True
    return False

def temEspecial(senha: str):
    for char in senha:
        if not char.isalnum():
            return True
    return False

def main():
    while True:
        try:   
            senha = input()

            valida = False

            if 6 <= len(senha) <= 32 and temMaiuscula(senha) and temMinuscula(senha) and temNumero(senha) and not temEspecial(senha):
                valida = True

            if valida:
                print("Senha valida.")
            else:
                print("Senha invalida.")

        except EOFError:
            break

main()