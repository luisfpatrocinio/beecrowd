// INCOMPLETA

#include <stdio.h>
#include <iostream>
 
bool interseccao(int x0, int y0, int x1, int y1, int x2, int y2, int x3, int y3) {
    bool interseccao_x = x0 > x3 || x1 > x2;    // X
    bool interseccao_y = y0 > y3 || y1 > y2;    // Y
    return interseccao_x && interseccao_y;
}

int main() {
    int x0, y0, x1, y1; // Coordenadas do primeiro retângulo
    int x2, y2, x3, y3; // Coordenadas do segundo retângulo

    std::cin >> x0 >> y0 >> x1 >> y1;
    std::cin >> x2 >> y2 >> x3 >> y3;

    if (interseccao(x0, y0, x1, y1, x2, y2, x3, y3)) {
        std::cout << 1 << std::endl; // Há interseção
    } else {
        std::cout << 0 << std::endl; // Não há interseção
    }

    return 0;
}