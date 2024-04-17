#include <stdio.h>
#include <iostream>
int main() {
    
    int value;
    std::cin >> value;
    for (int i = 1; i < value + 1; i++) {
        int a = i;
        int b = i * i;
        int c = i * i * i;
        std::cout << a << " ";
        std::cout << b << " ";
        std::cout << c << std::endl;
        
        std::cout << a << " ";
        std::cout << b+1 << " ";
        std::cout << c+1 << std::endl;
    }
 
    return 0;
}
