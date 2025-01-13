#include <stdio.h>

void printResults(int cobaias[], int total) {
    printf("Total: %d cobaias\n", total);
    printf("Total de coelhos: %d\n", cobaias[0]);
    printf("Total de ratos: %d\n", cobaias[1]);
    printf("Total de sapos: %d\n", cobaias[2]);
    printf("Percentual de coelhos: %.2f %%\n", (cobaias[0] / (float)total) * 100);
    printf("Percentual de ratos: %.2f %%\n", (cobaias[1] / (float)total) * 100);
    printf("Percentual de sapos: %.2f %%\n", (cobaias[2] / (float)total) * 100);
}

int main() {
    int n, qtd, total = 0;
    char tipo;
    int cobaias[3] = {0, 0, 0}; // 0 -> coelho, 1 -> rato, 2 -> sapo

    // leitura do número de casos de teste, e atribuindo a variável n
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d %c", &qtd, &tipo);
        total += qtd;

        if (tipo == 'C') {
            cobaias[0] += qtd; // Coelhos
        } else if (tipo == 'R') {
            cobaias[1] += qtd; // Ratos
        } else if (tipo == 'S') {
            cobaias[2] += qtd; // Sapos
        }
    }

    printResults(cobaias, total);

    return 0;
}
