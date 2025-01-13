#include <stdio.h>

int main() {
    int left = -1;
    int right = -1;
    
    while (left != 0 && right != 0) {
        scanf("%d %d", &left, &right);
        
        if (left != 0 && right != 0) {
            printf("%d", left + right);
        }
    }
}