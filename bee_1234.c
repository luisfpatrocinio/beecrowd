#include <stdio.h>
#include <ctype.h>

int ehMaiusculo(char c) {
    return c >= 'A' && c <= 'Z';
}

int ehMinusculo(char c) {
    return c >= 'a' && c <= 'z';
}

char tornarMaiusculo(char c) {
    return c - 32;
}

char tornarMinusculo(char c) {
    return c + 32;
}

char obterLetraMaiuscula(char c) {
    if (ehMaiusculo(c)) {
        return c;
    }
    return tornarMaiusculo(c);
}

int ehEspaco(char c) {
    return c == ' ';
}

int main() {
    char sentenca[1000];  // Ajuste o tamanho conforme necessário

    while (fgets(sentenca, sizeof(sentenca), stdin)) {
        int estado = 1;  // 0 - maiúscula, 1 - minúscula
        char novaSentenca[1000] = "";  // Ajuste o tamanho conforme necessário
        int novaPos = 0;

        for (int i = 0; sentenca[i] != '\0'; i++) {
            char charAtual = sentenca[i];

            if (ehEspaco(charAtual)) {
                novaSentenca[novaPos++] = charAtual;
                continue;
            }

            char novaLetra = (estado == 1) ? obterLetraMaiuscula(charAtual) : tornarMinusculo(obterLetraMaiuscula(charAtual));
            novaSentenca[novaPos++] = novaLetra;
            estado = (estado + 1) % 2;
        }

        novaSentenca[novaPos] = '\0';
        printf("%s", novaSentenca);
    }

    return 0;
}
