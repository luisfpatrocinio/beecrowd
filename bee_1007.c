#include <stdio.h>

int calcDiff(a, b, c, d) {
    return a * b - c * d;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int diferenca = calcDiff(a, b, c, d);
    printf("DIFERENCA = %d\n", diferenca);
    return 0;
}
