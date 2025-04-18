#include <stdio.h>

// função pra calcular o fatorial, coisa básica: só multiplicar os números de 1 até o n
unsigned long long factorial(int n) {
    unsigned long long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    int m, n;

    // enquanto ainda tiver coisa pra ler, continua processando
    while (scanf("%d %d", &m, &n) != EOF) {
        // soma os fatoriais dos dois números que foram lidos
        unsigned long long sum = factorial(m) + factorial(n);
        printf("%llu\n", sum); // manda a soma pra saída
    }

    return 0;
}