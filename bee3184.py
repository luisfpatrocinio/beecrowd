## INCOMPLETO

def temTrap(grid, x, y):
    for i in range(3):
        if i == 0:
            val = grid[y][x+1]
        if i == 1:
            val = grid[y-1][x]
        if i == 2:
            val = grid[y][x-1]
        if i == 3:
            val = grid[y+1][x]
        if val == "T":
            return True

def main():
    playerX = -1
    playerY = -1
    
    w, h = list(map(int, input().split()))
    levelGrid = []
    for i in range(h):
        thisLine = list(input())
        try:
            if thisLine.index("P"):
                playerX = thisLine.index("P")
                playerY = i
        except ValueError as peido:
            pass
              
        levelGrid.append(thisLine)

    print("Mapa gerado:")
    print(levelGrid)

    # Procurar o jogador
    while True:
        if temTrap(levelGrid, playerX, playerY):
            levelGrid[playerY, playerX] = "#"
            break
        else:
            pass


main()