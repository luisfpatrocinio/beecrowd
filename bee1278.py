# Nós temos alguns textos e queremos formatá-los e justificá-los à direita, ou seja, alinhar suas linhas à margem direita de cada um. Crie um programa que, após ler um texto, reimprima esse texto com apenas um espaço entre as palavras e suas linhas justificadas à direita em todo o texto.

# Entrada
# A entrada contém diversos casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 100) 
# que indica o número de linhas de texto que virão a seguir. Cada uma destas N linhas de texto contém de 1 a 50 letras 
# maiúsculas (‘A’-‘Z’) ou espaços (‘ ’). Todas as linhas de texto contém no mínimo uma letra. Poderá haver mais de um 
# espaço entre as palavras. É também possível haver espaços no início e no final da linha. O fim da entrada é indicado por N = 0.

# Saída
# Para cada caso de teste imprima o texto com apenas um espaço entre as palavras, e inserindo tantos espaços quanto forem 
# necessários à esquerda de cada linha do texto, para que elas apareçam alinhadas à margem direita daquele texto, e na 
# mesma ordem da entrada. Deixe uma linha em branco entre os casos de testes. Não imprima espaços no final de cada linha,
# nem espaços desnecessários à esquerda, de modo que pelo menos uma das linhas impressa em cada texto inicie com uma letra.

def main():
    numCasos = int(input())
    linhasDefinitivas = []
    while numCasos != 0:
        linhasCorrigidas = []

        # Criar espaço entre o caso anterior e o atual
        if len(linhasDefinitivas) != 0:
            linhasDefinitivas.append("")
            
        # Receber um texto para cada linha:
        for i in range(numCasos):
            texto = input()
            textoCorrigido = ajeitarTexto(texto)
            linhasCorrigidas.append(textoCorrigido)

        # Alinhar a direita cada linha
        tamanhoDaMaiorLinha = obterTamanhoDaLinhaMaisLonga(linhasCorrigidas)
        for i in range(len(linhasCorrigidas)):
            linhaAtual = linhasCorrigidas[i]
            tamanhoDaLinhaAtual = len(linhaAtual)
            qntEspacos = tamanhoDaMaiorLinha - tamanhoDaLinhaAtual
            textoDefinitivo = ""
            for n in range(qntEspacos):
                textoDefinitivo += " "
            textoDefinitivo += linhaAtual
            linhasDefinitivas.append(textoDefinitivo)

        # Pedir nova quantidade de linhas
        numCasos = int(input())
    
    # Printar resultados
    for i in range(len(linhasDefinitivas)):
        print(linhasDefinitivas[i])

def ajeitarTexto(texto):
    textoAjustado = ""
    textoSemEspacos = retirarEspacosDoTexto(texto)
    palavras = str(textoSemEspacos).split()
    qntDePalavras = len(palavras)
    for i in range(qntDePalavras):
        palavra = palavras[i]
        textoAjustado += palavra
        if i < qntDePalavras - 1:
            textoAjustado += " "
    return textoAjustado

def retirarEspacosDoTexto(texto):
    textoStripado = str(texto).strip()
    novoTexto = ""
    ignorando = False
    for char in textoStripado:
        if str(char).isspace():
            ignorando = True
        else:
            if ignorando:
                novoTexto += " "
                ignorando = False
            novoTexto += str(char)
    return novoTexto

def obterTamanhoDaLinhaMaisLonga(arrayDeTextos):
    maior = 0
    for linha in arrayDeTextos:
        tamanho = len(linha)
        if tamanho > maior:
            maior = tamanho
    return maior

main()