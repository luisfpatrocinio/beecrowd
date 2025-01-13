#include <stdio.h>

// Função para calcular o MDC entre dois números
int mdc(int a, int b) {
    if (b == 0) {
        return a;
    }
    return mdc(b, a % b);
}

int main() {
    int n, a, b;

    // Entrada da quantidade de casos de teste
    scanf("%d", &n);

    // Para cada caso de teste, ler dois números e calcular o MDC
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &a, &b);
        printf("%d\n", mdc(a, b));
    }

    return 0;
}
