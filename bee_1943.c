#include <stdio.h>

int main() {
    int k;
    scanf("%d", &k);

    int tops[] = {1, 3, 5, 10, 25, 50, 100};
    int i, len = sizeof(tops) / sizeof(tops[0]);

    for(i = 0; i < len; i++) {
        if(k <= tops[i]) {
            printf("Top %d\n", tops[i]);
            break;
        }
    }

    return 0;
}
