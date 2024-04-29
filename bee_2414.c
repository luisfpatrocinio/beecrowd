#include <stdio.h>

int main() {
    int numeros[100];
    int n = 0;
    
    // Lendo os números
    while (1) {
        scanf("%d", &numeros[n]);
        
        if (numeros[n] == 0) {
            break;
        }
        n++;
        
    }

    int max = numeros[0];
    for (int i = 1; i < n; i++) {
        if (numeros[i] > max) {
            max = numeros[i];
        }
    }

    printf("%d\n", max);

    return 0;
}

