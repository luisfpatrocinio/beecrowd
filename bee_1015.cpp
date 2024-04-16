#include <stdio.h>
#include <cmath>
#include <iomanip>
#include <iostream>
 
int main() {
    // Coordenadas:
    double x1, y1, x2, y2;

    // Obter inputs:
    std::cin >> x1 >> y1;
    std::cin >> x2 >> y2;

    // Calcular distancia
    double distancia = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

    // Definindo a precisão para 4 casas decimais
    std::cout << std::fixed << std::setprecision(4);

    // Saída:
    std::cout << distancia << std::endl;
 
    return 0;
}