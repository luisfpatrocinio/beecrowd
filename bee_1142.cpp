#include <stdio.h>
#include <iostream>
 
int main() {
    
    int n;
    std::cin >> n;

    int x = 0;
    for (int i = 0; i < n; i++) {
        x++;
        std::cout << x << " ";
        x++;
        std::cout << x << " ";
        x++;
        std::cout << x << " ";
        std::cout << "PUM" << std::endl;
        x++;
    }
 
    return 0;
}