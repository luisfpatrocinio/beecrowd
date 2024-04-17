#include <stdio.h>
int main() {
    
    int value;
    scanf("%d", &value);
    for (int i = 1; i < value + 1; i++) {
        int a = i;
        int b = i * i;
        int c = i * i * i;

        printf("%d %d %d\n", a, b, c);
        printf("%d %d %d\n", a, b+1, c+1);
    }
 
    return 0;
}