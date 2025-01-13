#include <stdio.h>
#include <math.h>

int main() {
    int numero;
    scanf("%d", &numero);
    int brancas = (int) (pow(numero, 2) / 2) + (int) (numero % 2 != 0);
    int pretas = pow(numero, 2) / 2;

    printf("%d casas brancas e %d casas pretas", brancas, pretas);

    return 0;
}

/*
def main():
    numero = int(input())
    brancas = (int) (pow(numero, 2) / 2) + (int) (numero % 2 != 0);
    pretas = numero ** 2 // 2
    print(f"{brancas} casas brancas e {pretas} casas pretas")

main()
*/