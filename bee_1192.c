#include <stdio.h>

int main() {
    int numCasos;
    scanf("%d", &numCasos);
    00
    for (int i = 0; i < numCasos; i++) {
        char entrada[4];
        scanf("%s", entrada);
        
        int digito1 = entrada[0] - '0';
        int digito2 = entrada[2] - '0';
        
        if (digito1 == digito2) {
            printf("%d\n", digito1 * digito2);
        } else if (entrada[1] >= 'A' && entrada[1] <= 'Z') {
            printf("%d\n", digito2 - digito1);
        } else {
            printf("%d\n", digito2 + digito1);
        }
    }
    
    return 0;
}
