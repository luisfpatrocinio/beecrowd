#include <iostream>
#include <iomanip> // necessário para manipulação de precisão

int main() {
    double raio;
    std::cin >> raio;
    
    double pi = 3.14159;
    double area = pi * raio * raio;

    std::cout << "A=" << std::fixed << std::setprecision(4) << area << std::endl;
    
    return 0;
}