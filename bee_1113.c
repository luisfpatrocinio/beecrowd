#include <stdio.h>
int main() {
    while (1) {
        int num1, num2;
        scanf("%d", &num1);
        scanf("%d", &num2);

        if (num1 == num2) {
            // encerra
            break;
        }
        
        if (num1 < num2) {
            printf("Crescente\n");
        } else {
            printf("Decrescente\n");
        }
    }

    return 0;
}