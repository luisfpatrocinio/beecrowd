#include <stdio.h>

// só verifica se x é ímpar ou par e retorna o próximo número par
int main()
{
    unsigned int x;
    scanf("%u", &x);

    // se for ímpar, adiciona 1. se já for par, só soma 2
    unsigned int nextEven = (x % 2 == 0) ? x + 2 : x + 1;
    printf("%u\n", nextEven); // imprime o próximo número par

    return 0;
}