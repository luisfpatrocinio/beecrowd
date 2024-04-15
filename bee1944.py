# BRINDE FACE 2015
class Pilha:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.items.pop()
        
    def peek(self):
        if self.isEmpty():
            return -1
        else:
            return self.items[-1]
    
    def size(self):
        return len(self.items)


def reiniciarPilha(pilha: Pilha):
    pilha.push("F")
    pilha.push("A")
    pilha.push("C")
    pilha.push("E")

# A B C D
# D C B A
# A B C D

def verificarPontuacao(pilha: Pilha):
    tempArray = []
    if pilha.size() >= 8:
        for i in range(8):
            tempArray.append(pilha.pop())
    
    retorno = False

    if len(tempArray) >= 8:
        retorno = (tempArray[0] == tempArray[7] and tempArray[1] == tempArray[6] and tempArray[2] == tempArray[5] and tempArray[3] == tempArray[4])

    if not retorno:
        while (len(tempArray) > 0):
            pilha.push(tempArray.pop())
    
    return retorno

def main():
    pontuacao = 0   
    painel = Pilha()
    reiniciarPilha(painel)

    visitantes = int(input())
    for i in range(visitantes):
        combinacao = list(input().split())
        painel.push(combinacao[0])
        painel.push(combinacao[1])
        painel.push(combinacao[2])
        painel.push(combinacao[3])

        if verificarPontuacao(painel):
            pontuacao += 1

        if painel.size() == 0:
            reiniciarPilha(painel)

    print(pontuacao)


main()