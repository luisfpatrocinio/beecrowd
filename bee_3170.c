#include <stdio.h>
#include <math.h>

int main() {
    int qntBolinhas, qntGalhos;
    
    // Leitura da quantidade de bolinhas e galhos
    scanf("%d", &qntBolinhas);
    scanf("%d", &qntGalhos);

    // Cálculo da quantidade de bolinhas necessárias
    int bolasPrecisa = floor(qntGalhos / 2);
    int bolasFaltam = bolasPrecisa - qntBolinhas;

    // Verifica se faltam bolinhas e imprime o resultado
    if (bolasFaltam > 0) {
        printf("Faltam %d bolinha(s)\n", bolasFaltam);
    } else {
        printf("Amelia tem todas bolinhas!\n");
    }

    return 0;
}
