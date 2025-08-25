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

    // Arrays estáticos
    char nomes[x][21];
    float altura[x];
    bool aprovacao[x];

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

}