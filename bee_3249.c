// Runtime Error
// *** stack smashing detected ***: terminated
// timeout: the monitored command dumped core

#include <stdio.h>
#include <string.h>

int main()
{
    int qntBatalhas, qntVitorias = 0;
    scanf("%d", &qntBatalhas);
    for (int i = 0; i < qntBatalhas; i++)
    {
        char batalha[200];
        scanf("%200s", batalha);
        if (strstr(batalha, "CD") == NULL)
        {
            qntVitorias++;
        }
    }
    printf("%d\n", qntVitorias);
    return 0;
}