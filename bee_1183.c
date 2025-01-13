#include <stdio.h>

int main() {
    char op;
    scanf(" %c", &op);

    float matriz[12][12];

    // Leitura da matriz
    for (int i = 0; i < 12; i++) {
        for (int j = 0; j < 12; j++) {
            scanf("%f", &matriz[i][j]);
        }
    }

    float soma = 0;
    int cont = 0;

    // Cálculo da soma ou média dos elementos acima da diagonal principal
    for (int i = 0; i < 12; i++) {
        for (int j = i + 1; j < 12; j++) {
            soma += matriz[i][j];
            cont++;
        }
    }

    if (op == 'S') {
        printf("%.1f\n", soma);
    } else if (op == 'M') {
        printf("%.1f\n", soma / cont);
    }

    return 0;
}
