#include <iostream>
#include <iomanip>

int main() {
    double notaA, notaB, media;

    std::cin >> notaA >> notaB;

    media = (notaA * 3.5 + notaB * 7.5) / 11.0;

    // Definir 5 caasas decimais
    std::cout << std::fixed << std::setprecision(5);

    std::cout << "MEDIA = " << media << std::endl;

    return 0;
}
