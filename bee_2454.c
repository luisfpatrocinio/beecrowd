#include <stdio.h>

int main() {
    int p, r;
    scanf("%d %d", &p, &r);

    int result = -1;
    if (p == 0) {
        result = 2;
    } else {
        if (r == 0) {
            result = 1;
        } else {
            result = 0;
        }
    }

    char results[] = {'A', 'B', 'C'};
    printf("%c\n", results[result]);

    return 0;
}
