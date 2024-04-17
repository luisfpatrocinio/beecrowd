#include <stdio.h>
 
int main() {
    
    int x, m;
    scanf("%d %d", &x, &m);
    
    while (x != 0 && m != 0) {
        printf("%d\n", m * x);
        scanf("%d %d", &x, &m);
    }
 
    return 0;
}