#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


typedef struct Aluno
{
    char* Nome;
    float Altura;
    bool Aprovado;

} Aluno;


void start(Aluno *aluno)
{
    aluno->Nome = (char*)malloc(21 * sizeof(char));

    return;
}

void readAluno(Aluno *temp)
{
    scanf("%s", temp->Nome);
    scanf("%f", &temp->Altura);
    
    int aprovado;
    scanf("%d", &aprovado);
    temp->Aprovado = (aprovado != 0);

    return;
}

void printAluno(Aluno *aluno) {
    printf("Nome: %s\n", aluno->Nome);
    printf("Altura: %.2f\n", aluno->Altura);
    printf("Status: %s\n", aluno->Aprovado ? "Aprovado\n" : "Reprovado\n");
}


int main()
{
    int x;

    scanf("%d", &x);

    Aluno alunos[x];

    //aloca os alunos
    for(int i = 0; i < x; i++)
    {
        start(&alunos[i]);
    }

    //lê os alunos
    for(int i = 0; i < x; i++)
    {
        readAluno(&alunos[i]);
    }

    // Impressão dos alunos
    for(int i = 0; i < x; i++) {
        printAluno(&alunos[i]);
    }

    // Liberação de memória
    for(int i = 0; i < x; i++) {
        free(alunos[i].Nome);
    }
}