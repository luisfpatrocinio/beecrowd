#include <stdio.h>
 
int main() {
    
    int n;
    scanf("%d", &n);

    int x = 0;
    for (int i = 0; i < n; i++) {
        x++;
        printf("%d ", x);
        x++;
        printf("%d ", x);
        x++;
        printf("%d ", x);
        printf("PUM\n");
        x++;
    }
 
    return 0;
}