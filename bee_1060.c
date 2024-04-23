#include <stdio.h>
 
int main() {
 
    // Entrada
    int positivos = 0;
    for (int i = 0; i < 6; i++) {
        float numero;
        scanf("%f", &numero);
        if (numero > 0) {
            positivos++;
        }
    }
    // Saída
    printf("%d valores positivos\n", positivos);
    
    return 0;
}