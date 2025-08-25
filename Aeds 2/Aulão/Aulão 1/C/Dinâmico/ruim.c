#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

//? Você tem x(int) alunos com Nome(string de ate 20 caracteres), Altura(float) e Aprovação(0 ou 1)


bool lerBool()
{
    int in;
    scanf("%d", &in);

    return (in == 1 ? true : false); //!operador ternário
}

int main()
{
    int x;
    scanf("%d", &x);

    //Alocação
    char** nomes = (char**)malloc(x * sizeof(char*));
    for(int i = 0; i < x; i++)
    {
        nomes[i] = (char*)malloc(21 * sizeof(char));
    }
    float* altura = (float*)malloc(x * sizeof(float));
    bool* aprovacao = (bool*)malloc(x * sizeof(bool));

    //Leitura
    for(int i = 0; i < x; i++)
    {
        scanf("%21s", nomes[i]);
        scanf("%f", &altura[i]);
        aprovacao[i] = lerBool();
    }

    //printar os alunos
    for(int i = 0; i < x; i++)
    {
        printf("Aluno: %s\nAltura: %.2f\n", nomes[i], altura[i]);
        if(aprovacao[i])
            puts("Status: Aprovado");
        else
            puts("Status: Reprovado");
        puts("");
    }

    // Liberar memória
    for(int i = 0; i < x; i++) {
        free(nomes[i]);
    }
    free(nomes);
    free(altura);
    free(aprovacao);

}