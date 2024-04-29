#include <stdio.h>

int main() {
    long int numTestes;
    scanf("%ld", &numTestes);
    
    for (int i = 0; i < numTestes; i++) {
        long int r1, r2;
        scanf("%ld %ld", &r1, &r2);
        printf("%ld\n", (r1 + r1 + r2 + r2) / 2);
    }
    
    return 0;
}