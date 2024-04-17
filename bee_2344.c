#include <stdio.h>

int main() {
    int nota;
    scanf("%d", &nota);

    char conceito = 'E';
    if (nota > 85) {
        conceito = 'A';
    } else if (nota > 60) {
        conceito = 'B';
    } else if (nota > 35) {
        conceito = 'C';
    } else if (nota > 0) {
        conceito = 'D';
    }
    printf("%c\n", conceito);
    
    return 0;    
}

