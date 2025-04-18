#include <stdio.h>
#include <math.h>

// lê os dados, calcula a diferença e decide quanto dinheiro precisa ser trocado
int main()
{
    int n;

    while (1)
    {
        scanf("%d", &n);
        if (n == 0)
            break; // sai quando n é 0

        double expenses[1000], total = 0, average;

        // lê os valores gastos por cada aluno
        for (int i = 0; i < n; i++)
        {
            scanf("%lf", &expenses[i]);
            total += expenses[i];
        }

        average = total / n; // calcula a média dos gastos

        double give = 0, take = 0;

        // ajusta quem deve receber e quem deve pagar
        for (int i = 0; i < n; i++)
        {
            double diff = expenses[i] - average;
            if (diff > 0)
            {
                give += floor(diff * 100) / 100; // arredonda pra menos
            }
            else
            {
                take += floor(-diff * 100) / 100; // arredonda pra menos
            }
        }

        // o resultado é o máximo entre as somas de quem dá ou recebe
        printf("$%.2lf\n", give > take ? give : take);
    }

    return 0;
}