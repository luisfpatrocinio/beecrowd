#include <stdio.h>

int main() {
    int x1, y1, x2, y2;
    while (1) {
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        if (x1 == 0 && y1 == 0 && x2 == 0 && y2 == 0) {
            return 0;
        }

        if (x1 == x2 && y1 == y2) {
            printf("0\n");
            continue;
        }

        // Checar diferença
        int difx = abs(x2 - x1);
        int dify = abs(y2 - y1);

        // Mesma linha ou coluna ou diagonal
        if (x1 == x2 || y1 == y2 || difx == dify) {
            printf("1\n");
            continue;
        }

        printf("2\n");
        continue;
    }
}