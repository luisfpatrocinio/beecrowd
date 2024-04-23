#include <stdio.h>
#include <math.h>

double binet(int n) {
    double a = pow(((1 + sqrt(5)) / 2), n);
    double b = pow(((1 - sqrt(5)) / 2), n);
    return (a - b) / sqrt(5);
}

int main() {
    int n;
    scanf("%d", &n);
    double binet_value = binet(n);
    printf("%.1f\n", binet_value);

    return 0;
}