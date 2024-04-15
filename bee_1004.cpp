#include <stdio.h>
#include <iostream>
 
int main() {
 
    int a;
    int b;
    std::cin >> a;
    std::cin >> b;

    int x = a * b;

    std::cout << "PROD = " << x << std::endl;

    return 0;
}