#include <stdio.h>
#include <iostream>

int main() {
 
    int senha;
    std::cin >> senha;
    while (senha != 2002) {
        std::cout << "Senha Invalida" << std::endl;
        std::cin >> senha;
    }
    std::cout << "Acesso Permitido" << std::endl;
 
    return 0;
}