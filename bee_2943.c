// INCOMPLETO
// Smider Pan

#include <stdio.h>



int obterProximoPredio(int *alturas, int predioAtual, int numeroPredios, int status) {
    int proximoPredio = predioAtual;
    int alturaAtual = alturas[predioAtual];

    if (status == 0) { // subindo
        for (int i = predioAtual + 1; i < numeroPredios; i++) {
            if (alturas[i] > alturaAtual) {
                proximoPredio = i;
                break;
            }
        }
    } else { // descendo
        for (int i = predioAtual + 1; i < numeroPredios; i++) {
            if (alturas[i] < alturaAtual) {
                proximoPredio = i;
                break;
            }
        }
    }

    return proximoPredio;
}

int main() {
    // # Entrada:
    // Número de prédios
    int numeroPredios;
    scanf("%d", &numeroPredios);

    // Alturas dos prédios
    int alturas[numeroPredios];
    for (int i = 0; i < numeroPredios; i++) {
        scanf("%d", &alturas[i]);
    }

    // # Processamento:
    // Quantidade de saltos efetuados
    int qntSaltos = 0;
    // Altura atual
    int alturaAtual = 0;
    // Status subindo (0) ou descendo(1)
    int status = 0;
    // Contar saltos
    obterProximoPredio(alturas, )

    // # Saída:
    printf("%d\n", qntSaltos);

    return 0;
}