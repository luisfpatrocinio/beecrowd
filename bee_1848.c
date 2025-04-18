#include <stdio.h>
#include <string.h>

// Ler cada linha da entrada.
// Converter piscadas do corvo ('*' = 1, '-' = 0) em número decimal.
// Quando ler "caw caw", salvar a soma acumulada e começar de novo.
// Repetir até ter os três números da loteria.

int convertBlinkToDecimal(char blink[4])
{
    int decimal = 0;
    for (int i = 0; i < 3; i++)
    {
        decimal = (decimal << 1) + (blink[i] == '*' ? 1 : 0);
    }
    return decimal;
}

int main()
{
    char input[10];
    int lotteryNumbers[3], sum = 0, count = 0;

    while (count < 3)
    {
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0'; // Remover o caractere de nova linha

        if (strcmp(input, "caw caw") == 0)
        {
            lotteryNumbers[count++] = sum;
            sum = 0;
        }
        else
        {
            sum += convertBlinkToDecimal(input);
        }
    }

    for (int i = 0; i < 3; i++)
    {
        printf("%d\n", lotteryNumbers[i]);
    }

    return 0;
}