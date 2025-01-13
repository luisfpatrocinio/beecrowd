#include <stdio.h>

int main() {
    int quantidade;
    int multiplos_2 = 0, multiplos_3 = 0, multiplos_4 = 0, multiplos_5 = 0;
    
    scanf("%d", &quantidade);
    int numeros[quantidade];
    
    for (int i = 0; i < quantidade; i++) {
        scanf("%d", &numeros[i]);
    }
    
    for (int i = 0; i < quantidade; i++) {
        if (numeros[i] % 2 == 0) multiplos_2++;
        if (numeros[i] % 3 == 0) multiplos_3++;
        if (numeros[i] % 4 == 0) multiplos_4++;
        if (numeros[i] % 5 == 0) multiplos_5++;
    }
    
    printf("%d Multiplo(s) de 2\n", multiplos_2);
    printf("%d Multiplo(s) de 3\n", multiplos_3);
    printf("%d Multiplo(s) de 4\n", multiplos_4);
    printf("%d Multiplo(s) de 5\n", multiplos_5);
    
    return 0;
}
