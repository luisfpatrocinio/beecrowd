#include <stdio.h>

void buildMatrix(int size, int matrix[][100])
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            int value = i < j ? i : j;
            value = value < size - i ? value : size - i - 1;
            value = value < size - j ? value : size - j - 1;
            matrix[i][j] = value + 1;
        }
    }
}

void printMatrix(int size, int matrix[][100])
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            printf("%3d", matrix[i][j]);
            if (j < size - 1)
            {
                printf(" ");
            }
        }
        printf("\n");
    }
    printf("\n");
}

int main()
{
    int matrix[100][100];
    int size;

    while (1)
    {
        scanf("%d", &size);
        if (size == 0)
        {
            break;
        }

        buildMatrix(size, matrix);
        printMatrix(size, matrix);
    }

    return 0;
}