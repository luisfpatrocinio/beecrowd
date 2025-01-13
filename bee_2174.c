#include <stdio.h>
#include <string.h>

int main() {
    int quantidade;
    char pomekons[151][100];
    int pomekonCount = 0;

    // obter a quantidade
    scanf("%d", &quantidade);
    getchar();  // limpa o buffer

    for (int i = 0; i < quantidade; i++) {
        char nomeDoPomekon[100];
        int existe = 0; // flag que guarda se o pomekon ja foi adicionado

        fgets(nomeDoPomekon, sizeof(nomeDoPomekon), stdin);
        nomeDoPomekon[strcspn(nomeDoPomekon, "\n")] = '\0'; // substitui \n por \0

        for (int j = 0; j < pomekonCount; j++) {
            if (strcmp(pomekons[j], nomeDoPomekon) == 0) {
                existe = 1;
                break;
            }
        }

        if (!existe) {
            strcpy(pomekons[pomekonCount], nomeDoPomekon);
            pomekonCount++;
        }
    }

    printf("Falta(m) %d pomekon(s).\n", 151 - pomekonCount);

    return 0;
}
