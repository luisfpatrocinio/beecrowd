# Apagando e Ganhando

def main():
    qntDigitos, qntCortes = list(map(int, input().split()))

    while qntDigitos != 0 and qntCortes != 0:
        numero = input()
        cortesEfetuados = 0
        while cortesEfetuados < qntCortes:
            # Criamos um array com os números N - D:
            arrayNumeros = []
            for i in range(0, len(numero) - (qntCortes - cortesEfetuados) + 1):
                num = numero[i]
                arrayNumeros.append(num)
            
            # Agora temos um vetor com os numeros
            # print(arrayNumeros)

            # Nesse array, vamos pegar o menor número antes do maior.
            # Encontrar índice do maior:
            # conjuntoInteiro = list(map(int, arrayNumeros))
            # maiorDoConjunto = max(conjuntoInteiro)
            # posicaoDoMaior = conjuntoInteiro.index(maiorDoConjunto)
            # print("O maior do conjunto é: ", maiorDoConjunto)
            # print("A posição do maior valor é: ", posicaoDoMaior)
            
            # Percorrer do zero até esse valor do indice
            novosAteALinha = []
            # for i in range(0, posicaoDoMaior):
            #     num = conjuntoInteiro[i]
            #     novosAteALinha.append(num)
            novosAteALinha = arrayNumeros

            # print("O conjunto dos numeros até a linha imaginaria", novosAteALinha)
            # print("Não temos mais linha imaginaria: ", novosAteALinha)

            # Matar o menor:
            menorDoConjuntoNovo = min(novosAteALinha)
            posicaoDoMenorDoConjuntoNovo = novosAteALinha.index(menorDoConjuntoNovo)
            
            # Formar um novo numero, porém sem o menor do conjunto novo.
            novoNumero = ""
            for i in range(len(numero)):
                if i == posicaoDoMenorDoConjuntoNovo:
                    continue
                novoNumero += numero[i]

            # print("Cortamos o numero. Agora temos:")
            # print(novoNumero)
            numero = novoNumero
            cortesEfetuados += 1
        print(numero)
        qntDigitos, qntCortes = list(map(int, input().split()))
    

main()