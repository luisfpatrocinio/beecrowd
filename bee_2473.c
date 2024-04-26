#include <stdio.h>

#define MAX_NUM 6

int main() {
    int aposta[MAX_NUM];
    int sorteados[MAX_NUM];
    int acertos = 0;

    // Lendo as apostas
    for (int i = 0; i < MAX_NUM; i++) {
        scanf("%d", &aposta[i]);
    }

    // Lendo os números sorteados
    for (int i = 0; i < MAX_NUM; i++) {
        scanf("%d", &sorteados[i]);
    }

    // Verificando os acertos
    for (int i = 0; i < MAX_NUM; i++) {
        for (int j = 0; j < MAX_NUM; j++) {
            if (aposta[i] == sorteados[j]) {
                acertos++;
                break;
            }
        }
    }

    // Determinando o resultado
    if (acertos >= 6) {
        printf("sena\n");
    } else if (acertos >= 5) {
        printf("quina\n");
    } else if (acertos >= 4) {
        printf("quadra\n");
    } else if (acertos >= 3) {
        printf("terno\n");
    } else {
        printf("azar\n");
    }

    return 0;
}
