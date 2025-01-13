#include <stdio.h>

int main() {
    float notas[2];
    int count, x;

    while (1) {
        count = 0;

        // Loop para pegar duas notas válidas
        while (count < 2) {
            float nota;
            scanf("%f", &nota);

            if (nota >= 0 && nota <= 10) {
                notas[count] = nota;
                count++;
            } else {
                printf("nota invalida\n");
            }
        }

        // Calcula e printa a média das duas notas
        printf("media = %.2f\n", (notas[0] + notas[1]) / 2);

        // Pergunta se o usuário quer realizar um novo cálculo
        while (1) {
            printf("novo calculo (1-sim 2-nao)\n");
            scanf("%d", &x);

            if (x == 1 || x == 2) {
                break;
            }
        }

        if (x == 2) {
            break;  // Encerra se a resposta for '2'
        }
    }

    return 0;
}
