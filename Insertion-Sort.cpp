#include <cstdio>
#include <cstdlib>
#include <ctime>

void print_array(int C[], int tam)
{
    printf("[");
    for (int i = 0; i < tam - 1; i++)
    {
        printf("%d, ", C[i]);
    }
    printf("%d]", C[tam - 1]);
}
void insertion_sort(int C[], int tam, int print_ok)
{
    int changes = 0;
    int i, j, chave;
    if (print_ok)
    {
        printf("\nArray before: ");
        print_array(C, 10);
    }
    for (j = 1; j < tam; j++)
    {
        // Declara a chave como o valor do elemento em análise.
        chave = C[j];

        // Declara i como o índice anterior ao índice do elemento em análise.
        i = j - 1;

        // Laço que percorre o vetor partindo da esquerda do elemento em análise.
        // Enquanto i for maior ou igual à zero, ou seja, o laço roda até o fim do vetor.
        // Enquanto o valor do elemento de índice i for maior que o valor da chave, ou seja, o laço roda até achar um elemento de valor menor do que o valor do elemento em análise.
        while ((i >= 0) && (C[i] > chave))
        {
            // Move o elemento da direita para a esquerda.
            C[i + 1] = C[i];

            // Decrementa o i.
            i--;

            // Encrementa o número de mudanças.
            changes++;
        }
        // Saímos do laço, então o valor do elemento à esquerda é menor do que o valor em análise ou chegamos ao fim do vetor.
        /// A chave é salva na posição correta e continuamos a iteração do for usando j.
        C[i + 1] = chave;
    }
    if (print_ok)
    {
        printf("\nArray after: ");
        print_array(C, 10);
    }
    printf("\nInsertion Sort used %d changes.\n", changes);
}

int main()
{
    srand((unsigned)time(0));

    int arr1[10] = {12, 2, 5, 4, 8, 7, 6, 9, 1, 15};
    int arr2[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int arr3[10] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    int arr4[1000];
    int arr5[1000];

    insertion_sort(arr1, 10, 1);
    insertion_sort(arr2, 10, 1);
    insertion_sort(arr3, 10, 1);

    for (int i = 0; i < 1000; i++)
    {
        arr4[i] = 1000 - i;
    }
    insertion_sort(arr4, 1000, 0);
    for (int i = 0; i < 1000; i++)
    {
        arr5[i] = rand() % 1000 + 1;
    }
    insertion_sort(arr5, 1000, 0);
    for (int i = 0; i < 1000; i++)
    {
        arr5[i] = rand() % 1000 + 1;
    }
    insertion_sort(arr5, 1000, 0);

    return 0;
}
