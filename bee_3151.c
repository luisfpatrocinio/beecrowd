
#include <stdio.h>

int main() {
    int H, Z, L;
    scanf("%d %d %d", &H, &Z, &L);

    if ((H < Z && Z < L) || (L < Z && Z < H)) {
        printf("zezinho\n");
    } else if ((Z < H && H < L) || (L < H && H < Z)) {
        printf("huguinho\n");
    } else {
        printf("luisinho\n");
    }

    return 0;
}