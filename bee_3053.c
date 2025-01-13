#include <stdio.h>

int main()
{
    // Entrada: Número de ações.
    int n;
    scanf("%d", &n);

    // Limpar o buffer.
    getchar(); // Isso consome o '\n' após a entrada do número

    // Entrada: Onde a moeda vai estar
    char posInicialChar;
    scanf("%c", &posInicialChar);

    // Obtemos a posição inicial em 0, 1 ou 2.
    int posInicial = posInicialChar - 65;

    // Onde a moeda está atualmente.
    int posAtual = posInicial;

    // Para cada ação...
    for (int i = 0; i < n; i++)
    {
        // Perguntar para o usuário qual ação.
        int acao;
        scanf("%d", &acao);
        getchar();

        // Executar troca de acordo com a ação escolhida.
        switch (acao)
        {
        case 1:
            // Troca o A com o B.
            if (posAtual != 2)
            {
                posAtual++;
                posAtual = posAtual % 2;
            }
            break;
        case 2:
            if (posAtual != 0)
            {
                posAtual++;
                posAtual = 1 + ((posAtual + 1) % 2);
            }
            break;
        case 3:
            if (posAtual != 1)
            {
                posAtual += 2;
                posAtual = posAtual % 4;
            }
            break;
        }
    }

    // Printar onde está a moeda:
    char caractere = posAtual + 65;
    printf("%c\n", caractere);

    return 0;
}