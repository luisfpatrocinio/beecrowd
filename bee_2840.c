#include <stdio.h>
#include <math.h>

int main() {
    int r, l;
    scanf("%d %d", &r, &l);
    float volume = 4.0 / 3.0 * 3.1415 * pow(r, 3);
    printf("%d\n", (int)(l / volume));
    return 0;
}