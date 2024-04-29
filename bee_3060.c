#include <stdio.h>

int main() {
    int valorDaCompra, numParcelas;
    scanf("%d", &valorDaCompra);
    scanf("%d", &numParcelas);

    int resto = valorDaCompra % numParcelas;
    int i;

    for (i = 0; i < numParcelas; i++) {
        int thisResto = (resto > 0) ? 1 : 0;
        printf("%d\n", (valorDaCompra / numParcelas) + thisResto);
        resto--;;
    }

    return 0;
}
