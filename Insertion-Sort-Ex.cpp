#include <cstdio>
#include <cstdlib>

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
        printf("\n\n");
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
        if (print_ok){
            print_array(C, 10);
            printf("\n");
        }
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
    int arr6[16] = {32, 7, 3, 15, 13, 4, 21, 6, 2, 9, 1, 31, 45, 11, 5, 8};
    insertion_sort(arr6, 16, 1);

    return 0;
}