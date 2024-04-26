#include <stdio.h>

int main() {
    int hora_inicial, minuto_inicial, hora_final, minuto_final;
    
    // Entrada
    scanf("%d %d %d %d", &hora_inicial, &minuto_inicial, &hora_final, &minuto_final);

    // Processamento
    int duracao_hora, duracao_minuto;
    if (hora_inicial < hora_final) {
        duracao_hora = hora_final - hora_inicial;
    } else {
        duracao_hora = (24 - hora_inicial) + hora_final;
    }

    if (minuto_inicial < minuto_final) {
        duracao_minuto = minuto_final - minuto_inicial;
    } else {
        duracao_minuto = (60 - minuto_inicial) + minuto_final;
        duracao_hora -= 1;
    }

    if (duracao_minuto == 60) {
        duracao_minuto = 0;
        duracao_hora += 1;
    }

    if (duracao_hora == 24 && duracao_minuto > 0) {
        duracao_hora = 0;
    }

    // Saída
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", duracao_hora, duracao_minuto);

    return 0;
}
