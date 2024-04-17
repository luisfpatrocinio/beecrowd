#include <stdio.h>
#include <iostream>
#include <iomanip>
 
int main() {
 
    double f1, f2;
    std::cin >> f1 >> f2;

    double total = f1 + f2;

    double flutuacao = 1 / total;

    std::cout << std::fixed << std::setprecision(6);
    std::cout << flutuacao << std::endl;

    return 0;
}