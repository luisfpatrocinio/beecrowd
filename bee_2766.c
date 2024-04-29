#include <stdio.h>

int main() {
    char nomes[10][100]; 
    int i;

    // Lendo os nomes
    for (i = 0; i < 10; i++) {
        scanf("%s", nomes[i]);
    }

    // Imprimindo os nomes nos índices especificados
    printf("%s\n", nomes[2]);
    printf("%s\n", nomes[6]);
    printf("%s\n", nomes[8]);

    return 0;
}
