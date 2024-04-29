#include <stdio.h>

int estaDentro(int x, int y, int comprimento, int largura) {
    float step = (float)largura / comprimento;
    return y <= step * x;
}

int main() {
    int comprimento, largura, numSoldados;
    scanf("%d %d %d", &comprimento, &largura, &numSoldados);

    int time1[numSoldados];
    int time2[numSoldados];
    int time1_count = 0;
    int time2_count = 0;

    for (int i = 0; i < numSoldados; i++) {
        int x, y, s;
        scanf("%d %d %d", &x, &y, &s);

        if (!estaDentro(x, y, comprimento, largura)) {
            time1[time1_count++] = s;
        } else {
            time2[time2_count++] = s;
        }
    }

    int somatime1 = 0;
    for (int i = 0; i < time1_count; i++) {
        somatime1 += time1[i];
    }

    int somatime2 = 0;
    for (int i = 0; i < time2_count; i++) {
        somatime2 += time2[i];
    }

    printf("%d %d\n", somatime1, somatime2);

    return 0;
}