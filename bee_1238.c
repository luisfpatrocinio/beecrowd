#include <stdio.h>
#include <string.h>

int main() {
    int numCasos;
    scanf("%d", &numCasos);

    for (int i = 0; i < numCasos; i++) {
        char word1[50], word2[50];
        scanf("%s %s", word1, word2);

        int len1 = strlen(word1);
        int len2 = strlen(word2);
        int maxLen = len1 > len2 ? len1 : len2;

        char result[101]; // tamanho de cada palavra + 1 do terminador

        int charAtual = 0;

        for (int n = 0; n < maxLen; n++) {
            if (n < len1) {
                result[charAtual] = word1[n];
                charAtual++;
            }
            if (n < len2) {
                result[charAtual] = word2[n];
                charAtual++;
            }
        }

        result[charAtual] = '\0'; // terminador nulo

        printf("%s\n", result);
    }

    return 0;
}