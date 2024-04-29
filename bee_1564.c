#include <stdio.h>

int main() {
    while (1) {
        // Enquanto não tiver acabado o arquivo:
        int n;
        if (scanf("%d", &n) == EOF) {
            // Encerrar while loop
            break;
        }
        // Se não houver reclamações
        if (n == 0) {
            printf("vai ter copa!\n");
        }
        // Se reclamar, vai ter duas
        else {
            printf("vai ter duas!\n");
        }
    }

    return 0;
}