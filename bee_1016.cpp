#include <stdio.h>
#include <iostream>
 
int main() {
 
    float vel = 0.50;
    int dist;
    
    std::cin >> dist;

    int tempo = dist * vel;

    std::cout << tempo << " minutos" << std::endl;
 
    return 0;
}