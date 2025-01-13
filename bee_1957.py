v = int(input())

restos = []
restoAtual = v
while restoAtual >= 16:
    resto = restoAtual % 16
    restos.append(resto)
    restoAtual = restoAtual // 16

restos.append(restoAtual)

hexadecimal = ""
for i in range(len(restos)):
    resto = restos[len(restos) - i - 1]
    if resto < 10:
        hexadecimal += str(resto)
    else:
        hexadecimal += chr(ord('A') + resto - 10)

print(hexadecimal)