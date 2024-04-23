#include <stdio.h>
#include <math.h>

int main() {
    while (1) {
        int h1, m1, h2, m2;
        scanf("%d %d %d %d", &h1, &m1, &h2, &m2);

        // Encerrar programa:
        if (h1 == 0 && m1 == 0 && h2 == 0 && m2 == 0) {
            break;
        }

        int minutos1 = h1 * 60 + m1;
        int minutos2 = h2 * 60 + m2;

        int minutos;
        if (minutos2 >= minutos1) {
            minutos = minutos2 - minutos1;
        } else {
            minutos = 24 * 60 - minutos1 + minutos2;
        }
        
        printf("%d\n", minutos);
    }

    return 0;
}