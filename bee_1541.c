#include <stdio.h>
#include <math.h>

// Calcula a área da casa multiplicando comprimento e largura.
// Acha a área mínima do terreno dividindo a área da casa pelo percentual permitido.
// Calcula o lado do terreno como a raiz quadrada da área mínima.
// Converte o lado do terreno pra inteiro.
// Repete até que algum valor de entrada seja 0.

int main() {
    int length, width, percentage;

    while (1) {
        scanf("%d %d %d", &length, &width, &percentage);
        if (length == 0 || width == 0 || percentage == 0) {
            break;
        }

        // área da casa
        int houseArea = length * width;

        // área mínima do terreno necessária
        double minLandArea = (double)houseArea / (percentage / 100.0);

        // tamanho do lado do terreno
        int side = (int)sqrt(minLandArea);
        printf("%d\n", side);
    }

    return 0;
}