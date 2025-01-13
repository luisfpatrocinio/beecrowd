#include <stdio.h>
#include <stdlib.h>

int main() {
    int I;
    scanf("%d", &I);

    printf("Feliz nat");
    for (int i = 0; i < I; i++) {
        putchar('a');
    }
    printf("l!\n");

    return 0;
}
