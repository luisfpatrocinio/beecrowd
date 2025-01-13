def obterLinhaPeca(pecaStr) -> int:
    return int(pecaStr[0]) - 1

def obterColunaPeca(pecaStr) -> int:
    return int(ord(pecaStr[1])) - 97

def posicionarPeca(tipoPeca: str, pecaStr: str, grid: list):
    # Destrinchar:
    linha = obterLinhaPeca(pecaStr)
    coluna = obterColunaPeca(pecaStr)
    grid[linha][coluna] = tipoPeca
    # print(f"Peca: {tipoPeca} na linha {linha} e coluna {coluna}.")

## Retorna se o espaço determinado é válido ou não.
def consultarComprometimento(x, y, grid):
    if x < 0: return -1
    if x > len(grid) - 1: return -1
    if y < 0: return -1
    if y > len(grid) - 1: return -1
    return int(grid[y][x] == "X") * -1

def comprometerTabuleiro(grid: list):
    for y in range(1, len(grid)):
        for x in range(len(grid[y])):
            cell = grid[y][x]
            if cell == "P":
                # É peão, comprometer zonas de ataque:
                if x > 0:                   grid[y - 1][x - 1] = "X"
                if x < len(grid[y]) - 1:    grid[y - 1][x + 1] = "X"

    return grid

def main():
    numCaso = 0
    while True:
        numCaso += 1
        cavalo = input()
        if cavalo == "0":
            break

        # Criar tabuleiro vazio
        grid = [[' ' for _ in range(8)] for _ in range(8)]

        # Posicionar Cavalo
        posicionarPeca("C", cavalo, grid)

        # Posicionar Peões
        for _ in range(8):
            posicionarPeca("P", input(), grid)            

        # Comprometer tabuleiro com base nos peões:
        grid = comprometerTabuleiro(grid)

        # TESTE: Printar tabuleiro
        # for i in range(len(grid)):
        #     print(grid[i])

        # Contar bons movimentos
        movimentos = 8
        
        yc = obterLinhaPeca(cavalo)
        xc = obterColunaPeca(cavalo)

        # consultar movimentos
        for i in range(8):
            match i:
                case 0:
                    nxc = xc - 1
                    nyc = yc - 2
                case 1:
                    nxc = xc + 1
                    nyc = yc - 2
                case 2:
                    nxc = xc + 2
                    nyc = yc - 1
                case 3:
                    nxc = xc + 2
                    nyc = yc + 1
                case 4:
                    nxc = xc - 1
                    nyc = yc + 2
                case 5:
                    nxc = xc + 1
                    nyc = yc + 2
                case 6:
                    nxc = xc - 2
                    nyc = yc - 1
                case 7:
                    nxc = xc - 2
                    nyc = yc + 1
            movimentos += consultarComprometimento(nxc, nyc, grid)
    
        # Saída:
        print(f"Caso de Teste #{numCaso}: {movimentos} movimento(s).")
main()



